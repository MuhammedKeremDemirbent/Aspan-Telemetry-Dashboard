from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('mainpage.urls')),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('simulation/', include('simulation.urls')),
]
