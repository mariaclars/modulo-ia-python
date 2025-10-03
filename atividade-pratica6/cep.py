import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resultado = requests.get(url)
        resultado.raise_for_status()
        dados = resultado.json()
        
        if "erro" in dados:
            raise ValueError("Cep não encontrado.")
        
        logradouro = dados["logradouro"]
        bairro = dados["bairro"]
        cidade = dados["localidade"]
        estado = dados["uf"]
        
        print(f"{logradouro}, {bairro}, {cidade}, {estado}.")
        
    except Exception as error:
        print(f"Ocorreu o erro: {error}")
        
digite_cep = input("\nDigite seu cep: ").strip().replace("-", "")
consulta_cep(digite_cep)