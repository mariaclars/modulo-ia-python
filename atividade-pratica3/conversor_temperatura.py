#- Conversor de Temperatura
#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

unidade_medida_temp = float(input("\nQuantos graus está fazendo? "))
escala_origem = int(input("\nQual a escala de medida?\n1 - Celsius\n2 -Fahrenheit\n3- Kelvin\nDigite um numero: "))
escala_destino = int(input("\nPara qual escala deseja converter?\n1 - Celsius\n2 -Fahrenheit\n3- Kelvin\nDigite um numero: "))

#Celsius para Fahrenheit
if escala_origem == 1 and escala_destino == 2:
    conversao = (unidade_medida_temp * 1.8) + 32
    print(f"{conversao}°F")
#Celsius para Kelvin    
elif escala_origem == 1 and escala_destino == 3:
    conversao = unidade_medida_temp + 273.15
    print(f"{conversao}K")
#Fahrenheit para Celsius
elif escala_origem == 2 and escala_destino == 1:
    conversao = (unidade_medida_temp - 32) * 5/9
    print(f"{conversao}°C")
#Farenheit para Kelvin
elif escala_origem == 2 and escala_destino == 3:
    conversao = (unidade_medida_temp - 32) * 5/9 + 273.15
    print(f"{conversao}K")
#Kelvin para Celsius
elif escala_origem == 3 and escala_destino == 1:
    conversao = unidade_medida_temp - 273.15
    print(f"{conversao}°C")
#Kelvin para Farenheit
elif escala_origem == 3 and escala_destino == 2:
    conversao = (unidade_medida_temp - 273.15) * 1.8 + 32
    print(f"{conversao}°F")
#Tratamento de erro
else:
    ("Escolha inválida.")