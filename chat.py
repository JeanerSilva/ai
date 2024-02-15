import openai
from secret import apikey
openai.api_key = apikey
from helpers import *


def obter_resposta_subtopicos(subtópico):
    messages_resposta = [
        {"role": "system", "content": "Você é um assistente que explica subtópicos em detalhes de modo a prover uma pessoa que fará concurso público"},
        {"role": "user", "content": f"fale exaustivamente sobre o seguinte subtópico: {subtópico}. Se forem citados tipos, subtipos, classificações, tendências ou grupos, fale detidamente sobre cada um deles e cite exemplos."}
    ]
    response_resposta = openai.ChatCompletion.create(
        #model="gpt-4",
        model="gpt-3.5-turbo",
        messages=messages_resposta,
        temperature=0.1,
        max_tokens=1024,
        frequency_penalty=1.0
    )
    return response_resposta['choices'][0]['message']['content'].strip()

def gerar_subtopicos_e_perguntas(pergunta, contexto):
    try:
        messages = [
            {"role": "system", "content": "Você é um assistente que gera subtópicos a partir de tópicos. Os subtópicos são os mais relevantes para elaboração de questões de concursos"},
            {"role": "user", "content": f"Dado o seguinte tema: '{pergunta.strip()}', liste importantes subtópicos relacionados."}
        ]

        response_subtopicos = openai.ChatCompletion.create(
            #model="gpt-3.5-turbo",  
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.1,
            max_tokens=20,
            # frequency_penalty=1.0
        )
        
        # Processar a resposta para extrair os subtópicos
        last_response = response_subtopicos['choices'][0]['message']['content']
        subtópicos = last_response.strip().split('\n')
        informacoes_subtopicos = []

        for subtópico in subtópicos:
            if subtópico:
                #print(subtópico)
                resposta_subtópico = obter_resposta_subtopicos(subtópico)
                #print(resposta_subtópico)
                informacoes_subtopicos.append((subtópico, resposta_subtópico))

        return informacoes_subtopicos
    except Exception as e:
        print(f"Erro ao gerar subtopicos e perguntas: {e}")
        return []

def processar_perguntas(nome_arquivo, contexto):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        perguntas = arquivo.readlines()

    for pergunta in perguntas:
        arquivo =  sanitize_filename(pergunta[:-2]) + ".txt"
        with open("respostas/" + arquivo, 'a', encoding='utf-8') as arquivo_respostas:
            informacoes_subtopicos = gerar_subtopicos_e_perguntas(pergunta, contexto)
            arquivo_respostas.write(f"Item do edital: {pergunta} \n")
            for i, (subtópico, resposta_subtópico) in enumerate(informacoes_subtopicos, start=1):
                arquivo_respostas.write(f"{i}. Subtópico: {subtópico}\n{resposta_subtópico}\n")
            arquivo_respostas.write("\n")

contexto = carrega("contexto.txt")

processar_perguntas('perguntas.txt', contexto)

