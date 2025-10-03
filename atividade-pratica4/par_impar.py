 #Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos."""

par = 0
impar = 0
cont = 0
    
try:
    while cont >= 0:
        numero = int(input("\nDigite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            par += 1
        else:
            print(f"O número {numero} é impar.")
            impar += 1
        while True:
            continua = input("\nDeseja digitar outro número? S/N: ").upper()
            if continua == "S":
                cont += 1
                break
            elif continua == "N":
                cont = -1
                break
            else:
                print("Opção inválida! Digite apenas S ou N.")
except ValueError:
    print("Esse não é um número valido.")
finally:
    print(f"Foram digitados {par} números pares e {impar} números impar.")