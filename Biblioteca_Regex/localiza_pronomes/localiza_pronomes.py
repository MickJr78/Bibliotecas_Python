import re

# Lê o arquivo de pronomes e cria uma lista de pronomes
with open('C:/Users/Dev Junior Barbosa/OneDrive/Área de Trabalho/ESTUDOS_BIBLIOTECAS_PYTHON/Biblioteca_Regex/localiza_pronomes/pronomes.txt', encoding="utf-8-sig") as pronomes:
    lista_pronomes = [pron.strip() for pron in pronomes.read().split(',')]

# Lê o arquivo de texto
with open('C:/Users/Dev Junior Barbosa/OneDrive/Área de Trabalho/ESTUDOS_BIBLIOTECAS_PYTHON/Biblioteca_Regex/localiza_pronomes/texto2.txt', encoding="utf-8-sig") as arquivo:
    arquivo_texto = arquivo.read()

# Busca pelos pronomes no conteúdo do texto
regex_pronomes = r'\b(' + '|'.join(re.escape(pron) for pron in lista_pronomes) + r')\b'
busca = re.compile(regex_pronomes, re.IGNORECASE)  # O re.IGNORECASE permite buscar sem diferenciar maiúsculas de minúsculas
result = busca.findall(arquivo_texto)

# Exibe os pronomes encontrados
print(result)