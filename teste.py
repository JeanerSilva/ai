
subtópicos = ['- Conceito de kanban:', '  - Definição de kanban;', '  - Origem do kanban;', '  - Princípios do kanban;', '  - Benefícios do kanban;', '  - Limitações do kanban.', '', '- Implementação do kanban:', '  - Planejamento da implementação do kanban;', '  - Etapas para implementar o kanban;', '  - Definição de limites de trabalho;', '  - Criação de quadros kanban;', '  - Definição de cartões kanban;', '  - Estabelecimento de políticas de fluxo;', '  - Monitoramento e controle do kanban.', '', '- Tipos de kanban:', '  - Kanban de produção;', '  - Kanban de movimentação;', '  - Kanban de fornecimento;', '  - Kanban de sinalização;', '  - Kanban eletrônico.', '', '- Práticas ágeis relacionadas ao kanban:', '  - Kanban e Scrum;', '  - Kanban e Lean;', '  - Kanban e DevOps;', '  - Kanban e Agile.', '', '- Exemplos de aplicação do kanban:', '  - Kanban na indústria;', '  - Kanban na área de serviços;', '  - Kanban na gestão de projetos;', '  - Kanban na área de TI;', '  - Kanban na área de saúde.', '', '- Ferramentas e softwares para kanban:', '  - Trello;', '  - Jira;', '  - Kanbanize;', '  - LeanKit;', '  - Kanban Tool.', '', '- Casos de sucesso com kanban:', '  - Toyota e o sistema kanban;', '  - Casos de empresas que implementaram o kanban com sucesso;', '  - Resultados alcançados com a adoção do kanban.', '', '- Desafios e problemas comuns no uso do kanban:', '  - Resistência à mudança;', '  - Falta de comprometimento;', '  - Dificuldade em definir políticas de fluxo;', '  - Problemas de comunicação;', '  - Falta de acompanhamento e monitoramento adequados.']

retorno = ""
for subtópico in subtópicos:
    subtópico_corrigido = subtópico.replace("  - ", "-").replace("- ", "---")
    retorno = retorno + subtópico_corrigido
subtópicos = retorno.split('---')

#for subtópico in subtópicos_corrigidos:
#    print(subtópico)
print(subtópicos)