from datetime import datetime

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ContaPagarForm
from .models import ContaPaga, ContaPagar


def definir_contas(request: HttpRequest) -> HttpResponse:
    form = ContaPagarForm()

    if request.method == 'POST':
        form = ContaPagarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta cadastrada com sucesso.')
            return redirect(to='definir_contas')

    return render(request, 'definir_contas.html', {'form': form})


def ver_contas(request: HttpRequest) -> HttpResponse:
    MES_ATUAL = datetime.now().month
    DIA_ATUAL = datetime.now().day

    contas_a_pagar = ContaPagar.objects.all()
    contas_pagas = ContaPaga.objects.filter(data_pagamento__month=MES_ATUAL).values(
        'conta'
    )
    # contas_pagas = ContaPaga.objects.filter(data_pagamento__day__lte=DIA_ATUAL).values('conta')
    contas_vencidas = contas_a_pagar.filter(dia_de_pagamento__lt=DIA_ATUAL).exclude(
        id__in=contas_pagas
    )

    contas_proximas_do_vencimento = contas_a_pagar.filter(
        dia_de_pagamento__lte=DIA_ATUAL + 5, dia_de_pagamento__gte=DIA_ATUAL
    ).exclude(id__in=contas_pagas)

    contas_restantes = (
        contas_a_pagar.exclude(id__in=contas_vencidas)
        .exclude(id__in=contas_pagas)
        .exclude(id__in=contas_proximas_do_vencimento)
    )

    context = {
        'contas_vencidas': contas_vencidas,
        'contas_proximas_do_vencimento': contas_proximas_do_vencimento,
        'contas_restantes': contas_restantes,
    }
    return render(request, 'ver_contas.html', context)
