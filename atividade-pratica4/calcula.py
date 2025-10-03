#1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = input("Digite a operação, entre as opções (+ - * /): ")
    
    if operacao not in ["+", "-", "*", "/"]:
        raise KeyError("Operação inválida, as válidas são: + - * /")
    
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2

except ValueError:
    print("Erro: Entrada inválida, digite um número inteiro, ex: 10.")
except KeyError as keyerror:
    print(f"Erro: {keyerror}")
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")
else:
    print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")