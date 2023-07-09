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


# Função para converter URLs relativos em caminhos absolutos do sistema (para gerar pdf)
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
    """

    import os

    from django.conf import settings

    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ''))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ''))
    else:
        return uri

    # make sure that file exists
    # if not os.path.isfile(path):
    #     raise Exception(
    #         f'media URI must start with {sUrl} or {mUrl}'
    #     )

    return path