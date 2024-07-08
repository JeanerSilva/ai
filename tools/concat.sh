#!/bin/bash

# Arquivo que contém a lista de arquivos a serem concatenados
lista="d.txt"

# Arquivo de saída
saida="Desenvolvimento2.txt"

# Limpa o arquivo de saída se já existir
> $saida

# Lê cada linha do arquivo de lista e concatena os arquivos
while IFS= read -r arquivo
do
    cat "Desenvolvimento/$arquivo" >> $saida
done < "$lista"
