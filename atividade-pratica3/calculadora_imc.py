"""2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso" """


peso = float(input("\nDigite o seu peso: "))
altura = float(input("Qual a sua altura? "))

imc = peso / altura ** 2

if imc > 7 and imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está no peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >= 30:
    print("Você está obeso.")
else:
    print("imc inválido.")