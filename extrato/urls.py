from django.urls import path

from . import views


urlpatterns = [
    path('novo_extrato/', views.novo_extrato, name='novo_extrato'),
    path('ver_extratos/', views.ver_extratos, name='ver_extratos'),
]
