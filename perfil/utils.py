def calcula_total(instancia, campo):
    total = 0
    for i in instancia:
        total += getattr(i, campo)

    return total