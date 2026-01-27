from django.contrib import admin
from django.urls import path
from patrimonio.views import lista_bens  # ← IMPORTA VIEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_bens, name='home'),  # ← HOME DIRETO
]
