from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(ImportExportModelAdmin):
    list_display = ('numero_patrimonio', 'nome_patrimonio',
                    'status', 'localizacao')
    list_filter = ('status', 'categoria', 'localizacao')
    search_fields = ('numero_patrimonio', 'nome_patrimonio')
    list_per_page = 25


admin.site.register(CategoriaPatrimonio)
admin.site.register(Localizacao)
admin.site.register(Colaborador)
