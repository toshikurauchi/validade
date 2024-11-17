from django.urls import path

from core import views
from core import partial_views


urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:produto_id>/remover', views.remover, name='produto-remover'),
    path('partials/produto/<int:produto_id>', partial_views.define_quantidade, name='partial-produto-quantidade'),
    path('partials/produto/<int:produto_id>/diminuir', partial_views.diminui_quantidade, name='partial-produto-diminuir'),
    path('partials/produto/<int:produto_id>/aumentar', partial_views.aumenta_quantidade, name='partial-produto-aumentar'),
]
