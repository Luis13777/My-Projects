from django.urls import path
from app_INOA import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ativos/", views.ativos, name="ativos"),
    path("adicionar_ativo/", views.adicionar_ativo, name="adicionar_ativo"),
    path("excluir_ativo/<int:ativo_id>/", views.excluir_ativo, name="excluir_ativo"),
    path("atualizar_ativo/<int:ativo_id>/", views.atualizar_ativo, name="atualizar_ativo"),
    path("ativar_rastreador", views.ativar_rastreador, name="ativar_rastreador"),
    path("desativar_rastreador", views.desativar_rastreador, name="desativar_rastreador"),
    path("alterar_email", views.alterar_email, name="alterar_email"),
    path("imprimir_dados", views.imprimir_dados, name="imprimir_dados"),
]
