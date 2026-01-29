from django.shortcuts import render
from .models import BemPatrimonial

def lista_patrimonio(request):
    bens = BemPatrimonial.objects.all().order_by('-criado_em')
    return render(request, 'patrimonio/list.html', {'bens': bens})
