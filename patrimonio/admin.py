from django.contrib import admin
from .models import BemPatrimonial

@admin.register(BemPatrimonial)
class BemAdmin(admin.ModelAdmin):
    list_display = ['numero_tombo', 'numero_nf', 'descricao', 'tipo', 'valor', 'secretaria', 'departamento', 'gerente_patrimonio']
    list_filter = ['tipo', 'secretaria', 'departamento']
    search_fields = ['numero_tombo', 'descricao']
    list_editable = ['secretaria']
