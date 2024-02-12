
#from openai import OpenAI
import openai

openai.api_key =='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'
from helpers import *


def gerar_subtopicos_e_perguntas(pergunta, contexto):
    try:
        messages = [
            {"role": "system", "content": "You are a knowledgeable assistant who generates questions based on given topics."},
            {"role": "user", "content": f"Dado o seguinte tema: '{pergunta.strip()}', liste os 10 mais importantes subtópicos relacionados."}
        ]

        response_subtopicos = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=messages
        )
        
        # Processar a resposta para extrair os subtópicos
        last_response = response_subtopicos['choices'][0]['message']['content']
        subtópicos = last_response.strip().split('\n')
        perguntas_subtopicos = []

        for subtópico in subtópicos:
            if subtópico:
                messages_subtopico = [
                    {"role": "system", "content": "You are a knowledgeable assistant who generates questions based on given subtopics."},
                    {"role": "user", "content": f"Dado o subtópico: '{subtópico}', gere uma pergunta relevante."}
                ]
                response_pergunta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages_subtopico
                )
                pergunta_gerada = response_pergunta['choices'][0]['message']['content'].strip()
                perguntas_subtopicos.append((subtópico, pergunta_gerada))

        return perguntas_subtopicos
    except Exception as e:
        print(f"Erro ao gerar subtopicos e perguntas: {e}")
        return []

def processar_perguntas(nome_arquivo, contexto):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        perguntas = arquivo.readlines()

    with open('respostas.txt', 'a', encoding='utf-8') as arquivo_respostas:
        for pergunta in perguntas:
            perguntas_subtopicos = gerar_subtopicos_e_perguntas(pergunta, contexto)
            arquivo_respostas.write(f"Pergunta Original: {pergunta}")
            for i, (subtópico, pergunta_gerada) in enumerate(perguntas_subtopicos, start=1):
                arquivo_respostas.write(f"{i}. Subtópico: {subtópico} - Pergunta: {pergunta_gerada}\n")
            arquivo_respostas.write("\n")

contexto = carrega("contexto.txt")

processar_perguntas('perguntas.txt', contexto)
