from django.contrib import admin
from django.urls import path, include
from patrimonio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_patrimonio, name='lista_patrimonio'),
    path('accounts/', include('django.contrib.auth.urls')),
]
