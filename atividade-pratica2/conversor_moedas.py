#Conversor e moedas: Real para Dólar e Euro
  #Valores das Moedas
valor_em_reais = float(input("Digite o valor em reais para a conversão: "))
cotacao_dolar = 5,20
cotacao_euro = 6,15

  #Conversão 
conversao_em_dolares = valor_em_reais / cotacao_dolar
conversao_em_euros = valor_em_reais / cotacao_euro

  #Exibição dos Resultados
print(f"Saldo em Reais: R$ {valor_em_reais:.2f}")
print(f"Valor em Dolares: $ {conversao_em_dolares:.2f}")
print(f"Valor em Euro £ {conversao_em_euros:.2f}")