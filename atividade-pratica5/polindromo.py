def palindromo(palavra: str):
    letras_da_palavra = list(palavra)  # transforma em lista de letras
    letras_da_palavra.reverse()        # inverte a lista
    palavra_ao_contrario = "".join(letras_da_palavra)  # junta sem espaços
    
    if palavra == palavra_ao_contrario:
        return f"Sim, a palavra {palavra} é um palíndromo."
    else:
        return f"A palavra {palavra} não é um palíndromo."

print(palindromo("arara"))
print(palindromo("python"))