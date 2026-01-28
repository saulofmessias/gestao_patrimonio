from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BemPatrimonial


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def list_bens(request):
    bens = BemPatrimonial.objects.all()
    return render(request, 'list_bens.html', {'bens': bens})


@login_required
def add_bem(request):
    return render(request, 'add_bem.html')


@login_required
def detail_bem(request, pk):
    bem = BemPatrimonial.objects.get(numero_patrimonio=pk)
    return render(request, 'detail_bem.html', {'bem': bem})
