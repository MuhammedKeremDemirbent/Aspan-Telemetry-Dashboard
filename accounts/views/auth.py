from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def login(request):
    # Eğer kullanıcı zaten giriş yapmışsa direkt anasayfaya yönlendir
    if request.user.is_authenticated:
        return redirect('home')

    # Oturum süresi dolduğu için yönlendirilmişse (next parametresi varsa) uyarı göster
    if 'next' in request.GET:
        # Mesajlar birikmesin diye mevcut mesajları temizlemek gerekebilir veya sadece bir kez gösterilir
        # Django messages framework bunu genellikle yönetir.
        messages.warning(request, 'Oturum süreniz sonlanmıştır, lütfen tekrar giriş yapın.')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Hatalı e-posta veya şifre girdiniz!')
            
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')
