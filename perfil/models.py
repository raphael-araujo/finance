from django.db import models
from django.db.models import Sum

# Create your models here.


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejado = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    def total_gasto(self):
        from datetime import datetime

        from extrato.models import Extrato

        extratos = Extrato.objects.filter(
            categoria__id=self.id, data__month=datetime.now().month
        ).aggregate(Sum('valor'))
        return extratos['valor__sum'] if extratos['valor__sum'] else 0

    def percentual_gasto_por_categoria(self):
        try:
            return (self.total_gasto() * 100) / self.valor_planejado
        except:
            return 0

    def __str__(self) -> str:
        return self.categoria


class Conta(models.Model):
    BANCO_CHOICES = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa econômica'),
        ('BB', 'Banco do Brasil'),
        ('IT', 'Itaú'),
    )
    TIPO_CHOICES = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=BANCO_CHOICES)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=30, decimal_places=2)
    icone = models.ImageField(upload_to='icones')

    def __str__(self) -> str:
        return self.apelido
