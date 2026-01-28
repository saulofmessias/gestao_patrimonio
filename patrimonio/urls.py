from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_bens, name='list_bens'),
    path('add/', views.add_bem, name='add_bem'),
    path('detail/<str:pk>/', views.detail_bem, name='detail_bem'),
]
