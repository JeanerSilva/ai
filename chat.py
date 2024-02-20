import openai
from secret import apikey
openai.api_key = apikey
from helpers import *


def gerar_subtopicos_e_perguntas(pergunta):
    try:
        messages = [
            {"role": "system", "content": "Você provê respostas completas para um estudante que precisa entender da matéria em detalhes"},
            {"role": "user", "content": f"{pergunta.strip()}"}
        ]

        response_subtopicos = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.1,
            max_tokens=1024,
        )

        last_response = response_subtopicos['choices'][0]['message']['content']
        print(f"last_response======: {last_response} ")

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
        with open("respostas/" + arquivo, 'a', encoding='utf-8') as arquivo_respostas:
            respostaGPT = gerar_subtopicos_e_perguntas(pergunta)
            print(f"informacoes_subtopicos {respostaGPT}")
            arquivo_respostas.write(f"Item do edital: {pergunta} \n")
            arquivo_respostas.write(f"{respostaGPT}\n ===")
            arquivo_respostas.write("\n")

processar_perguntas('perguntas.txt')

