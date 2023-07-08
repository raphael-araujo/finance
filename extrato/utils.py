from django.contrib import messages
from django.http import HttpRequest


def extrato_is_valid(
    request: HttpRequest,
    valor: str,
    categoria: str,
    descricao: str,
    data: str,
    conta: str,
    tipo: str,
) -> bool:

    if (
        len(valor.strip()) == 0
        or len(categoria.strip()) == 0
        or len(descricao.strip()) == 0
        or len(data.strip()) == 0
        or len(conta.strip()) == 0
        or len(tipo) == 0
    ):
        messages.error(request, message="Preencha todos os campos.")
        return False

    return True
