import json
from decimal import Decimal

from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from extrato.models import Categoria


def definir_planejamento(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'definir_planejamento.html', context)


@csrf_exempt
def update_valor_categoria(request: HttpRequest, id: int):
    novo_valor = json.load(request)['novo_valor']

    try:
        categoria = get_object_or_404(Categoria, id=id)
        categoria.valor_planejado = Decimal(novo_valor)
        categoria.save()
    except:
        messages.error(request, 'Erro interno do sistema.')
        return redirect('definir_planejamento')

    return JsonResponse({'status': 'Sucesso'})


def ver_planejamento(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    return render(request, 'ver_planejamento.html', {'categorias': categorias})
