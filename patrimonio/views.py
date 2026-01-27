from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BemPatrimonial
from django.db.models import Q

@login_required
def lista_bens(request):
    query = request.GET.get('q', '')
    bens = BemPatrimonial.objects.all()
    if query:
        bens = bens.filter(
            Q(numero_tombo__icontains=query) |
            Q(nome_patrimonio__icontains=query) |
            Q(secretaria__icontains=query)
        )
    return render(request, 'patrimonio/lista_bens.html', {'bens': bens, 'query': query})

@login_required
def adicionar_bem(request):
    if request.method == 'POST':
        # Lógica de formulário aqui (ou use CreateView)
        messages.success(request, 'Bem cadastrado!')
        return redirect('lista_bens')
    return render(request, 'patrimonio/adicionar_bem.html')

@login_required
def editar_bem(request, pk):
    bem = get_object_or_404(BemPatrimonial, pk=pk)
    # Lógica edição
    return render(request, 'patrimonio/editar_bem.html', {'bem': bem})
