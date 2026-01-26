from django.db import models


class BemPatrimonial(models.Model):
    numero_tombo = models.CharField(max_length=20)
    numero_nf = models.CharField(max_length=30, blank=True)
    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    data_compra = models.DateField(blank=True, null=True)

    SECRETARIAS = [
        ('admin', 'Secretaria Administração'),
        ('financas', 'Secretaria Finanças'),
        ('educacao', 'Secretaria Educação'),
        ('saude', 'Secretaria Saúde'),
        ('obras', 'Secretaria Obras'),
        ('patrimonio', 'Departamento Patrimônio'),
    ]
    localizacao = models.CharField(
        max_length=100, choices=SECRETARIAS, blank=True)

    departamento = models.CharField(
        max_length=100, blank=True)

    secretaria = models.CharField(
        max_length=20, choices=SECRETARIAS, blank=True)

    gerente_patrimonio = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.numero_tombo
