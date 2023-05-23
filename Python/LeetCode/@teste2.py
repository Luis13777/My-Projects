dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

valor_idade = dicionario.get("idade")
print(valor_idade)  # Output: 25

valor_genero = dicionario.get("genero")
print(valor_genero)  # Output: None

valor_genero = dicionario.get("genero", "Desconhecido")
print(valor_genero)  # Output: Desconhecido

dicionario["novo"] = 'teste'
print(dicionario['novo'])