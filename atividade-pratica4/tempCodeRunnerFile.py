def gorjeta(conta: float, porcentagem) -> float:
    resultado = conta * (porcentagem / 100)
    return resultado

print(gorjeta(500, 15))