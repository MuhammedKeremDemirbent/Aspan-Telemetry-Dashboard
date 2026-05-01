from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import User

def register(request):
    if request.method == 'POST':
        first_name    = request.POST.get('first_name', '').strip()
        last_name     = request.POST.get('last_name', '').strip()
        username      = request.POST.get('username', '').strip()
        email         = request.POST.get('email', '').strip()
        phone         = request.POST.get('phone', '').strip()
        password      = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        # Validasyonlar
        if not all([first_name, last_name, username, email, password]):
            messages.error(request, 'Lütfen zorunlu alanları doldurunuz!')
            return render(request, 'accounts/register.html')

        if password != password_confirm:
            messages.error(request, 'Şifreler birbiriyle eşleşmiyor!')
            return render(request, 'accounts/register.html')

        if len(password) < 8:
            messages.error(request, 'Şifre en az 8 karakter olmalıdır!')
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Bu e-posta adresi zaten kullanılıyor!')
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu kullanıcı adı zaten kullanılıyor!')
            return render(request, 'accounts/register.html')

        # Kullanıcıyı oluştur (şifre otomatik hashlenir)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        if phone:
            user.phone = phone
            user.save()

        messages.success(request, 'Hesabınız başarıyla oluşturuldu! Giriş yapabilirsiniz.')
        return redirect('login')

    return render(request, 'accounts/register.html')
