#!/bin/bash

# Função para concatenar arquivos em uma pasta e subpastas
concatenar_arquivos() {
    pasta=$1
    arquivo_concatenado="$pasta.txt"
    find "$pasta" -type f -exec cat {} + > "$arquivo_concatenado"
}

# Percorre todas as pastas e executa a função concatenar_arquivos
for pasta in */; do
    concatenar_arquivos "$pasta"
done
