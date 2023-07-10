from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ContaPagarForm


def definir_contas(request: HttpRequest) -> HttpResponse:
    form = ContaPagarForm()

    if request.method == 'POST':
        form = ContaPagarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta cadastrada com sucesso.')
            return redirect(to='definir_contas')

    return render(request, 'definir_contas.html', {'form': form})
