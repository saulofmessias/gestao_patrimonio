from django.contrib import admin
from django.urls import path, include
from patrimonio import views  # Adicione

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_patrimonio, name='lista_patrimonio'),  # Home
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
