import os
import re

# Caminho da pasta onde os arquivos .txt estão localizados
pasta_respostas = 'respostas'

# Substituições a serem feitas
substituicoes = {
    #r'#': ' ',
    #r'\*': ' ',
    #r'---': ' ',
    #r'::': ':',
    #r'>': '',
    r'===': ''
}

# Itera sobre todos os arquivos na pasta
for arquivo in os.listdir(pasta_respostas):
    if arquivo.endswith('.txt'):
        caminho_arquivo = os.path.join(pasta_respostas, arquivo)
        
        # Lê o conteúdo do arquivo
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
        
        # Realiza as substituições
        for padrao, substituicao in substituicoes.items():
            conteudo = re.sub(padrao, substituicao, conteudo)
        
        # Escreve o conteúdo modificado de volta no arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            file.write(conteudo)

print("Substituições concluídas!")
