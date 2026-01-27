from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import BemPatrimonial


class BemResource(resources.ModelResource):
    class Meta:
        model = BemPatrimonial
        fields = ('numero_tombo', 'numero_nf', 'descricao', 'tipo', 'valor',
                  'data_compra', 'localizacao', 'departamento', 'secretaria', 'gerente_patrimonio')
        export_order = fields


@admin.register(BemPatrimonial)
class BemAdmin(ImportExportModelAdmin):
    resource_class = BemResource
    list_display = ['numero_tombo', 'descricao',
                    'tipo', 'valor', 'localizacao', 'secretaria', 'status']
    list_filter = ['secretaria', 'status', 'tipo', 'localizacao']
    search_fields = ['numero_tombo', 'descricao', 'nome_patrimonio']
    list_editable = ['localizacao', 'status']
    list_per_page = 25
    ordering = ['numero_tombo']  # ← Ordena automático
