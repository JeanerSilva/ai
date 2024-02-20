#!/bin/bash

# Função para concatenar arquivos em uma pasta e subpastas
concatenar_arquivos() {
    pasta=$1
    arquivo_concatenado="$pasta.txt"
    nome_do_arquivo=$(echo "$arquivo_concatenado" | sed 's/\///g')
    echo $nome_do_arquivo
    find "$pasta" -type f -exec cat {} + > "$nome_do_arquivo"
}

# Percorre todas as pastas e executa a função concatenar_arquivos
for pasta in */; do
    concatenar_arquivos "$pasta"
done
