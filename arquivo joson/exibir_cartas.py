import json

# Abrindo o arquivo JSON e carregando seu conteúdo
with open('cartas.json', 'r', encoding='utf-8') as file:
    cartas_json = json.load(file)

# Convertendo o dicionário em uma string JSON formatada
cartas_str = json.dumps(cartas_json, indent=4, ensure_ascii=False)

# Exibindo o JSON formatado no console
print(cartas_str)