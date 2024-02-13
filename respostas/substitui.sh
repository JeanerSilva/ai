#!/bin/bash

# Função para substituir uma expressão por outra dentro de cada arquivo
replace_in_files() {
    folder="$1"
    find "$folder" -type f -name "*.txt" -exec sed -i 's/Pergunta Original:/Item do edital:/g' {} \;
}

# Navega para o diretório raiz onde estão os subdiretórios
#cd /caminho/do/diretorio/raiz

# Chama a função para substituir a expressão em cada subdiretório
for subfolder in */; do
    replace_in_files "$subfolder"
done
