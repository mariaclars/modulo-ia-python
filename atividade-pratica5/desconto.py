def calcular_desconto():
    
    valor_objeto = float(input("\nDigite o valor do objeto: "))
    porcentagem_desconto = int(input("Digite a porcentagem do desconto: "))
    
    valor_com_desconto = valor_objeto - (valor_objeto * porcentagem_desconto/100)
    
    print(f"\nO objeto custa R${valor_objeto:.2f} e tem {porcentagem_desconto}% de desconto, ficando com o preço final de R${valor_com_desconto:.2f}")

calcular_desconto()