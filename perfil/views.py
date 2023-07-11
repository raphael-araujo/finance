from django.contrib import messages
from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from extrato.models import Extrato

from .forms import CategoriaForm, ContaForm
from .models import Categoria, Conta
from .utils import calcula_total

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    contas = Conta.objects.all()
    saldo_total = calcula_total(contas, "valor")

    context = {
        "contas": contas,
        "saldo_total": saldo_total,
    }

    return render(request, "home.html", context)


def gerenciar_contas(request: HttpRequest) -> HttpResponse:
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    conta_form = ContaForm()
    categoria_form = CategoriaForm

    if request.method == "POST":
        conta_form = ContaForm(request.POST, request.FILES)
        if conta_form.is_valid():
            conta_form.save()
            messages.success(request, "Conta adicionada com sucesso.")
            return redirect(to="gerenciar_contas")

    valor_total = 0
    for conta in contas:
        valor_total += conta.valor

    context = {
        "contas": contas,
        "categorias": categorias,
        "conta_form": conta_form,
        "categoria_form": categoria_form,
        "valor_total": valor_total,
    }
    return render(request, "gerenciar_contas.html", context)


def deletar_banco(request: HttpRequest, id: int) -> HttpResponse:
    conta = get_object_or_404(Conta, id=id)
    conta.delete()

    messages.warning(request, "Conta removida com sucesso.")
    return redirect(to="gerenciar_contas")


def cadastrar_categoria(request: HttpRequest) -> HttpResponse:
    categoria_form = CategoriaForm(request.POST)

    if categoria_form.is_valid():
        categoria_form.save()
        messages.success(request, "Categoria cadastrada com sucesso.")
    return redirect(to="gerenciar_contas")


def atualizar_categoria(request: HttpRequest, id: int) -> HttpResponse:
    categoria = get_object_or_404(Categoria, id=id)
    categoria.essencial = not categoria.essencial
    categoria.save()

    return redirect(to="gerenciar_contas")


def dashboard(request: HttpRequest) -> HttpResponse:
    dados = {}
    categorias = Categoria.objects.all()

    for categoria in categorias:
        dados[categoria.categoria] = Extrato.objects.filter(
            categoria=categoria
        ).aggregate(Sum("valor"))["valor__sum"]

    context = {
        "labels": list(dados.keys()),
        "values": list(float(dado) for dado in dados.values())}

    return render(request, "dashboard.html", context)
