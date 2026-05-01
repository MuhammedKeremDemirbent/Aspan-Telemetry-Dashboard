from django.urls import path
from . import views

urlpatterns = [

    path('ttn-webhook/', views.ttn_webhook, name='ttn_webhook'), 
]
