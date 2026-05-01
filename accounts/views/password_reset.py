from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from accounts.models import User
from accounts.tasks import send_password_reset_email

def resetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        
        user = User.objects.filter(email=email).first()
        
        if user:
            # Güvenli token ve uid oluşturma
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Sıfırlama linkini hazırla
            reset_link = f"http://localhost:8001/accounts/reset-confirm/{uid}/{token}/"
            
            # Celery taskını asenkron tetikle
            send_password_reset_email.delay(user.email, reset_link, user.first_name)
            
            messages.success(request, 'Şifre sıfırlama bağlantısı e-posta adresinize gönderildi!')
        else:
            messages.error(request, 'Bu e-posta adresiyle kayıtlı bir kullanıcı bulunamadı!')
            
    return render(request, 'accounts/resetpassword.html')

def reset_confirm(request, uidb64, token):
    try:
        # uidb64 çözümleme ve kullanıcıyı bulma
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Token geçerli mi?
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('password')
            new_password_confirm = request.POST.get('password_confirm')

            if new_password == new_password_confirm:
                if len(new_password) >= 8:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, 'Şifreniz başarıyla güncellendi! Giriş yapabilirsiniz.')
                    return redirect('login')
                else:
                    messages.error(request, 'Şifre en az 8 karakter olmalıdır!')
            else:
                messages.error(request, 'Şifreler birbiriyle eşleşmiyor!')

        return render(request, 'accounts/reset_confirm.html', {'valid_link': True})
    else:
        return render(request, 'accounts/reset_confirm.html', {'valid_link': False})
