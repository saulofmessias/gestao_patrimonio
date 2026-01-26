from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import BemPatrimonial

@admin.register(BemPatrimonial)
class BemAdmin(ImportExportModelAdmin):  # ← ImportExport!
    list_display = ['numero_tombo', 'descricao', 'tipo', 'valor', 'localizacao', 'secretaria', 'departamento']
    list_filter = ['tipo', 'secretaria', 'departamento', 'localizacao']
    search_fields = ['numero_tombo', 'descricao']
    list_editable = ['departamento']
