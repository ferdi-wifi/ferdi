from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda_teknisi, name='beranda_teknisi'),
    
]
