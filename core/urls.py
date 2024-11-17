from django.urls import path

from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:produto_id>', views.define_quantidade, name='produto-quantidade'),
    path('produto/<int:produto_id>/diminuir', views.diminui_quantidade, name='produto-diminuir'),
    path('produto/<int:produto_id>/aumentar', views.aumenta_quantidade, name='produto-aumentar'),
    path('produto/<int:produto_id>/remover', views.remover, name='produto-remover'),
]
