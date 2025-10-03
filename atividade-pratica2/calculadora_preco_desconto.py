#Calculadora de descontos em uma loja

#Informações do produto
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o valor do produto: "))
porcentagem_desconto = int((input("Digite a porcentagem de desconto: ")))

#Calculo do desconto e preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

#Exibição dos resultados
print(f"Produto: {nome_produto}.")
print(f"Preço: {preco_original}.")
print(f"Desconto: {porcentagem_desconto}%.")
print(f"Valor do desconto: {valor_desconto:.2f}.")
print(f"Valor com desconto: {preco_final:.2f}.")