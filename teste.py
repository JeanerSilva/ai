
last_response = """ - Tópico: Conceito de macroeconomia
  - Subtópico: Definição de macroeconomia
  - Subtópico: Objetivos da macroeconomia
  - Subtópico: Principais indicadores macroeconômicos

- Tópico: Agregados monetários
  - Subtópico: Definição de agregados monetários
  - Subtópico: Tipos de agregados monetários
  - Subtópico: Funções dos agregados monetários na economia

- Tópico: Medição dos agregados monetários
  - Subtópico: Métodos de medição dos agregados monetários
  - Subtópico: Importância da medição dos agregados monetários
  - Subtópico: Limitações na medição dos agregados monetários

- Tópico: Relação entre agregados monetários e a economia
  - Subtópico: Influência dos agregados monetários na inflação
  - Subtópico: Impacto dos agregados monetários no crescimento econômico
  - Subtópico: Papel dos agregados monetários na política monetária

- Tópico: Política monetária
  - Subtópico: Definição de política monetária
  - Subtópico: Instrumentos da política monetária
  - Subtópico: Objetivos da política monetária

- Tópico: Importância dos agregados monetários para a política monetária
  - Subtópico: Utilização dos agregados monetários como indicadores econômicos
  - Subtópico: Relação entre os agregados monetários e as metas da política monetária
  - Subtópico: Avaliação dos agregados monetários na formulação da política monetária"""

if "\n\n" in last_response:
    subtópicos = last_response.strip().split('\n\n')
else:
    subtópicos = last_response.strip().split('\n')
#print(subtópicos)

for subtópico in subtópicos:
    subtópico = subtópico.replace("\n", "").replace("- Tópico: ", "").replace("  - Subtópico: ", ", ")
    print(f"{subtópico} \n")


#for subtópico in subtópicos_corrigidos:
#    print(subtópico)
