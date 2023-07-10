from django.db import models

from perfil.models import Categoria


class ContaPagar(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=30, decimal_places=2)
    dia_de_pagamento = models.IntegerField()

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name_plural = 'Contas a pagar'


class ContaPaga(models.Model):
    conta = models.ForeignKey(ContaPagar, on_delete=models.DO_NOTHING)
    data_pagamento = models.DateField()

    class Meta:
        verbose_name_plural = 'Contas pagas'
