from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import User

@login_required
def profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()

        # Basit Validasyon
        if not all([first_name, last_name, email]):
            messages.error(request, 'Ad, soyad ve e-posta alanları zorunludur!')
            return redirect('profile')

        # Email çakışma kontrolü
        if User.objects.filter(email=email).exclude(pk=request.user.pk).exists():
            messages.error(request, 'Bu e-posta adresi başka bir kullanıcı tarafından kullanılıyor!')
            return redirect('profile')

        # Güncelleme
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone = phone
        user.save()

        messages.success(request, 'Profil bilgileriniz başarıyla güncellendi!')
        return redirect('profile')

    return render(request, 'accounts/profile.html')
