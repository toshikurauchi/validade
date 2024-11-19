from django.urls import path

from core import views
from core import partial_views


urlpatterns = [
    path('', views.lista_produtos, name='lista-produtos'),
    path('produto', views.cadastro, name='cadastro'),
    path('tags', views.lista_tags, name='tags'),
    path('tags/<int:tag_id>', views.lista_tags, name='tag-editar'),
    path('tags/<int:tag_id>/remover', views.deleta_tag, name='tag-remover'),
    path('historico', views.historico, name='historico'),
    path('produto/<int:produto_id>/remover', views.remover, name='produto-remover'),
    path('produto/<int:produto_id>/restaurar', views.restaurar, name='produto-restaurar'),

    path('partials/produtos', partial_views.lista_produtos, name='partial-produtos'),
    path('partials/produto/<int:produto_id>', partial_views.produto_edit, name='partial-produto-editar'),
    path('partials/produto/<int:produto_id>/quantidade', partial_views.define_quantidade, name='partial-produto-quantidade'),
    path('partials/produto/<int:produto_id>/diminuir', partial_views.diminui_quantidade, name='partial-produto-diminuir'),
    path('partials/produto/<int:produto_id>/aumentar', partial_views.aumenta_quantidade, name='partial-produto-aumentar'),
]
