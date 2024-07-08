#!/bin/bash

# Pasta que contém os arquivos .txt

# Expressões a serem removidas
expressoes="#|**|Item do edital: "

# Loop para cada arquivo .txt na pasta
for arquivo in /mnt/c/Users/Administrador/Desktop/estrategia/gpt_api/respostas/*.txt; do
    # Verifica se o arquivo existe
    if [ -f "$arquivo" ]; then
        # Faz um backup do arquivo original
        cp "$arquivo" "$arquivo.bak"

        # Remove as expressões do conteúdo do arquivo
        sed -i "s/$expressoes//g" "$arquivo"

        # Verifica se houve alguma alteração no arquivo
        if diff "$arquivo" "$arquivo.bak" > /dev/null; then
            # Se não houver alterações, remove o backup
            rm "$arquivo.bak"
            echo "Nenhuma alteração feita em: $arquivo"
        else
            # Se houver alterações, informa o usuário
            echo "Alterações feitas em: $arquivo"
        fi
    fi
done
