# Função
def gorjeta(conta: float, porcentagem) -> float:
    resultado = conta * (porcentagem / 100)
    return resultado

print(gorjeta(500, 15))



# Função lambda
gorjeta = lambda conta, porcentagem : conta * (porcentagem / 100)
resultado = gorjeta(360, 10)

print(resultado)