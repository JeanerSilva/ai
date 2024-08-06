import openai
from secret import apikey
openai.api_key = apikey
from helpers import *


def cria_dissertacao(pergunta):
    try:
        messages = [
            {"role": "user", "content": f'''Estou estudando para um concurso e preciso de ajuda para entender melhor o conteúdo do meu edital. 
             Pode me fornecer um resumo conciso e direto ao ponto sobre o seguinte tópico do edital: {pergunta.strip()}? 
             Gostaria que o resumo incluísse os principais pontos, conceitos e aspectos essenciais sobre o tema.
             Se houver uma lista, indique todos seus itens sem resumir ou apenas citar exemplos'''}
        ]

        response_subtopicos = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.1,
            max_tokens=1024,
        )

        last_response = response_subtopicos['choices'][0]['message']['content']
        # print(f"last_response======: {last_response} ")

        return last_response
    except Exception as e:
        print(f"Erro ao gerar subtopicos e perguntas: {e}")
        return []

def processar_perguntas(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        perguntas = arquivo.readlines()

    for pergunta in perguntas:
        arquivo =  sanitize_filename(pergunta).replace("\n", "")
        if len(arquivo) > 100:
            arquivo = arquivo[:100] 
        arquivo = arquivo + ".txt"
        p = pergunta.split("::")[1]
        with open("respostas/" + arquivo, 'a', encoding='utf-8') as arquivo_respostas:
            print(f"{pergunta}")
            respostaGPT = cria_dissertacao(p)            
            arquivo_respostas.write(f"{p} -\n")
            arquivo_respostas.write(f"{respostaGPT}\n")
            arquivo_respostas.write("\n")

processar_perguntas('perguntas.txt')

#C:\Users\Administrador\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\python.exe .\chat.py
# C:\Users\Administrador\anaconda3\python.exe .\chat.py       