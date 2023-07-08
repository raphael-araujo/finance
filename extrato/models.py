from django.db import models

from perfil.models import Categoria, Conta


class Extrato(models.Model):
    TIPO_CHOICES = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )

    valor = models.DecimalField(max_digits=30, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    data = models.DateField()
    conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING, related_name='conta_extrato')
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    

    def __str__(self) -> str:
        return self.descricao
