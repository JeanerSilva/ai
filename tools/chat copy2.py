import os
import openai
from openai import OpenAI
from helpers import *

from secret import apikey

client = OpenAI(
    api_key=os.environ.get(apikey),
)


def cria_dissertacao(pergunta):
    try:
        message = [


            {"role": "user", "content": f'''Estou estudando para um concurso e preciso de ajuda para entender melhor o conteúdo do meu edital. 
             Pode me fornecer um resumo conciso e direto ao ponto sobre o seguinte tópico do edital: {pergunta.strip()}? 
             Gostaria que o resumo incluísse os principais pontos, conceitos e aspectos essenciais sobre o tema.
             Se houver uma lista, indique todos seus itens sem resumir ou apenas citar exemplos'''}
        ]

        response_subtopicos =  client.chat.completions.create(
            model="gpt-4o",
            messages=message,
        )

        last_response = response_subtopicos['choices'][0]['message']['content']

        return last_response
    except openai.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass
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
            # respostaGPT = p[1]
            respostaGPT = cria_dissertacao(pergunta)
            print(f"{pergunta}\n")
            arquivo_respostas.write(f"{pergunta}\n\n")
            arquivo_respostas.write(f"{respostaGPT}\n")
            arquivo_respostas.write("\n")

processar_perguntas('perguntas.txt')

