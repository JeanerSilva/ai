#!/bin/bash
# Função para substituir uma expressão por outra dentro de cada arquivo
for arquivo in *.txt; do
    # Verifica se o arquivo realmente existe (evita o problema com nenhum arquivo .txt)
    if [ -f "$arquivo" ]; then
        # Substitui todas as ocorrências de ** por "" diretamente no arquivo
        sed -i 's/\*\*//g' "$arquivo"
        echo "Expressões '**' substituídas por '\"\"' em: $arquivo"
    fi
done
