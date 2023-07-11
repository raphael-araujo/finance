def calcula_total(instancia, campo):
    total = 0
    for i in instancia:
        total += getattr(i, campo)

    return total


def calcula_equilibrio_financeiro():
    from datetime import datetime

    from extrato.models import Extrato

    gastos_essenciais = Extrato.objects.filter(data__month=datetime.now().month, tipo='S', categoria__essencial=True)
    gastos_nao_essenciais = Extrato.objects.filter(data__month=datetime.now().month, tipo='S', categoria__essencial=False)

    total_gastos_essenciais = calcula_total(gastos_essenciais, 'valor')
    total_gastos_nao_essenciais = calcula_total(gastos_nao_essenciais, 'valor')

    total = total_gastos_essenciais + total_gastos_nao_essenciais
    try:
        percentual_gastos_essenciais = total_gastos_essenciais * 100 / total
        percentual_gastos_nao_essenciais = total_gastos_nao_essenciais * 100 / total

        return percentual_gastos_essenciais, percentual_gastos_nao_essenciais
    except:
        return 0, 0
