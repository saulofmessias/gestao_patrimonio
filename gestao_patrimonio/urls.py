from django.contrib import admin
from django.urls import path
from patrimonio import views  # ← Adicione esta linha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_patrimonio, name='lista_patrimonio'),  # ← Home lista
    path('accounts/', include('django.contrib.auth.urls')),
]
