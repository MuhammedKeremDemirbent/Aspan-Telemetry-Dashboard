from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('reset-confirm/<uidb64>/<token>/', views.reset_confirm, name='password_reset_confirm'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]