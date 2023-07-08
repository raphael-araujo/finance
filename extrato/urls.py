from django.urls import path

from . import views


urlpatterns = [
    path('novo_extrato/', views.novo_extrato, name='novo_extrato'),
]
