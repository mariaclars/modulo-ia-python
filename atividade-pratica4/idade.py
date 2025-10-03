from datetime import date

def idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = date.today().year
    idade_em_anos = ano_atual - ano_nascimento
    idade_dias = idade_em_anos * 365
    return idade_dias

print(idade_em_dias(1986))