from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bens, name='lista_bens'),
    path('adicionar/', views.adicionar_bem, name='adicionar_bem'),
    path('editar/<int:pk>/', views.editar_bem, name='editar_bem'),
]
