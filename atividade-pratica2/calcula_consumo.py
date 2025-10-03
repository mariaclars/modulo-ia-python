#Calculadora de consumo de combustivel

#Dados da viagem
distancia_percorrida = int(input("Digite a distancia percorrida em km: "))
combustivel_gasto = int(input("Digite a quantidade de combustivel gasta, em litros: "))

#Cálculo de consumo
consumo = distancia_percorrida / combustivel_gasto

#Exibição dos resultados
print("Dados da viagem: ")
print(f"Distancia Percorrida: {distancia_percorrida}km")
print(f"Combutivel Gasto: {combustivel_gasto}lt")
print(f"Consumo Médio: {consumo:.2f}km/l")