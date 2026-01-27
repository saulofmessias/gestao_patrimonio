from django.db import models

class BemPatrimonial(models.Model):
    numero_tombo = models.CharField(max_length=20, unique=True)  # Único!
    nome_patrimonio = models.CharField(max_length=200)
    numero_nf = models.CharField(max_length=30, blank=True)
    descricao = models.TextField(max_length=500)
    tipo = models.CharField(max_length=50)  # Ex: Computador, Mesa, etc.
    quantidade = models.PositiveIntegerField(default=1)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    data_compra = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=[
        ('disponivel', 'Disponível'),
        ('em_uso', 'Em Uso'),
        ('manutencao', 'Manutenção'),
        ('baixa', 'Baixa'),
        ('inexistente', 'Inexistente'),
    ], default='disponivel')
    
    SECRETARIAS = [
        ('administracao', 'Administração'),
        ('financas', 'Finanças'),
        ('educacao', 'Educação'),
        ('saude', 'Saúde'),
        ('obras', 'Obras'),
        ('patrimonio', 'Patrimônio'),
    ]
    secretaria = models.CharField(max_length=20, choices=SECRETARIAS)
    departamento = models.CharField(max_length=100, blank=True)
    localizacao = models.CharField(max_length=200, blank=True)
    gerente_responsavel = models.CharField(max_length=100, blank=True)
    imagem = models.ImageField(upload_to='patrimonio/', blank=True, null=True)
    
    criado_em = models.DateTimeField(auto_now_add=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_tombo} - {self.nome_patrimonio}"
    
    class Meta:
        ordering = ['numero_tombo']
        verbose_name = "Bem Patrimonial"
        verbose_name_plural = "Bens Patrimoniais"
