from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.sales, name='sales'),
    path('info/', views.info, name='info'),
    path('settings/', views.settings, name='settings'),
    path('graphs/', views.graphs, name='graphs'),
]