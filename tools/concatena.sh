#!/bin/bash

# Diretório que contém os arquivos
diretorio="$1"

# Nome do arquivo de saída
arquivo_saida="$2"

# Verifica se o diretório foi informado
if [ -z "$diretorio" ]; then
  echo "Erro: Diretório não informado."
  exit 1
fi

# Verifica se o arquivo de saída foi informado
if [ -z "$arquivo_saida" ]; then
  echo "Erro: Nome do arquivo de saída não informado."
  exit 1
fi

# Verifica se o diretório existe
if [ ! -d "$diretorio" ]; then
  echo "Erro: Diretório '$diretorio' não existe."
  exit 1
fi

# Concatena os arquivos
for arquivo in "$diretorio"/*; do
  if [ -f "$arquivo" ]; then
    cat "$arquivo" >> "$arquivo_saida"
  fi
done

sed -i 's/===/ /g' "$arquivo_saida"
sed -i 's/`/ /g' "$arquivo_saida"

echo "Arquivos concatenados com sucesso em '$arquivo_saida'."