from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class CategoriaPatrimonio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Localizacao(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.TextField(blank=True)
    cidade = models.CharField(max_length=100, default='Capanema')
    gerente = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    funcao = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_completo


class BemPatrimonial(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('alocado', 'Alocado'),
        ('manutencao', 'Manutenção'),
        ('perdido', 'Perdido'),
        ('descartado', 'Descartado'),
    ]

    numero_patrimonio = models.CharField(max_length=20, unique=True)
    nome_patrimonio = models.CharField(max_length=200)
    imagem = CloudinaryField(
        'foto', folder='patrimonio_capanema/', blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=1)
    categoria = models.ForeignKey(
        CategoriaPatrimonio, on_delete=models.SET_NULL, null=True)
    custo_compra = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    data_compra = models.DateField(blank=True, null=True)
    localizacao = models.ForeignKey(
        Localizacao, on_delete=models.SET_NULL, null=True, blank=True)
    colaborador_responsavel = models.ForeignKey(
        Colaborador, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='disponivel')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_patrimonio} - {self.nome_patrimonio}"
