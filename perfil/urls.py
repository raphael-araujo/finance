from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gerenciar_contas/', views.gerenciar_contas, name='gerenciar_contas'),
    path('deletar_banco/<int:id>/', views.deletar_banco, name='deletar_banco'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('atualizar_categoria/<int:id>/', views.atualizar_categoria, name='atualizar_categoria'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
