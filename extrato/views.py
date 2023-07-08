from decimal import Decimal

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from perfil.models import Categoria, Conta

from .models import Extrato
from .utils import extrato_is_valid


def novo_extrato(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')

        if not extrato_is_valid(
            request, valor, categoria, descricao, data, conta, tipo
        ):
            return redirect(to='novo_extrato')

        try:
            novo_extrato = Extrato.objects.create(
                valor=valor,
                categoria_id=categoria,
                descricao=descricao,
                data=data,
                conta_id=conta,
                tipo=tipo,
            )
            novo_extrato.save()

            conta = get_object_or_404(Conta, id=conta)

            if tipo == 'E':
                conta.valor += Decimal(valor)
            else:
                conta.valor -= Decimal(valor)

            conta.save()

            messages.success(request, 'Extrato criado com sucesso')
            return redirect(to='novo_extrato')
        except:
            messages.error(request, 'Erro interno do sistema.')
            return redirect(to='novo_extrato')
    else:
        categorias = Categoria.objects.all()
        contas = Conta.objects.all()

        context = {
            'categorias': categorias,
            'contas': contas,
        }
        return render(request, 'novo_extrato.html', context)
