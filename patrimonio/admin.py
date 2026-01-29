from django.contrib import admin
from .models import *


@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('numero_patrimonio', 'nome_patrimonio', 'status')


admin.site.register(CategoriaPatrimonio)
admin.site.register(Localizacao)
admin.site.register(Colaborador)
