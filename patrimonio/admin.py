from django.contrib import admin
from .models import BemPatrimonial, CategoriaPatrimonio, Localizacao, Colaborador


@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('numero_patrimonio', 'nome_patrimonio', 'status')
    list_filter = ('status',)
    search_fields = ('numero_patrimonio',)


admin.site.register(CategoriaPatrimonio)
admin.site.register(Localizacao)
admin.site.register(Colaborador)
