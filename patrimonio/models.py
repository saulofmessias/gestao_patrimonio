from django.db import models
from cloudinary.models import CloudinaryField

class Patrimonio(models.Model):
    STATUS = (('ativo', 'Ativo'), ('manutencao', 'Manutenção'), ('descartado', 'Descartado'))
    
    nome = models.CharField(max_length=200)
    secretaria = models.CharField(max_length=100, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descricao = models.TextField(blank=True)
    data_aquisicao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='ativo')
    imagem = CloudinaryField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
