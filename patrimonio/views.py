from django.shortcuts import render
from django.http import HttpResponse
from .models import BemPatrimonial


def lista_bens(request):
    bens = BemPatrimonial.objects.all()
    html = """
    <h1>🏛️ Patrimônio Capanema</h1>
    <table border="1">
      <tr><th>Tombo</th><th>Nome</th><th>Secretaria</th></tr>
    """
    for bem in bens:
        html += f"<tr><td>{bem.numero_tombo}</td><td>{bem.nome_patrimonio}</td><td>{bem.secretaria}</td></tr>"
    html += "</table><a href='/admin/'>Admin</a>"
    return HttpResponse(html)
