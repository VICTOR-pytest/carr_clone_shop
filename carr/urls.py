from django.urls import path
from . import views

urlpatterns = [
    path('', views.carr_list, name='carr_list'),
    path('criar/', views.carr_criar, name='carr_criar'),
    path('<int:id>/', views.carr_detalhe, name='carr_detalhe'),
    path('<int:id>/editar/', views.carr_editar, name='carr_editar'),
    path('<int:id>/deletar/', views.carr_deletar, name='carr_deletar'),
]
