#!/bin/bash
# Função para substituir uma expressão por outra dentro de cada arquivo
replace_in_files() {
    folder="$1"
    antes="$2"
    depois="$3"
    expressao="s/$antes/$depois/g"
    # echo "Substitui $antes por $depois em $folder"
    find "$folder" -type f -name "*.txt" -exec sed -i "$expressao" {} \;
}


# Chama a função para substituir a expressão em cada subdiretório
for subfolder in */; do
    for i in {1..10}; do
        echo "$subfolder" "$i)" "$i."
        replace_in_files "$subfolder" "$i)" "$i."
    done
    # replace_in_files "$subfolder" "1)" "1."
    
done
