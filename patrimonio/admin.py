from django.contrib import admin
from .models import BemPatrimonial, CategoriaPatrimonio, Colaborador, Localizacao


@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'categoria', 'localizacao']
    list_filter = ['categoria', 'localizacao']


admin.site.register([CategoriaPatrimonio, Colaborador, Localizacao])
