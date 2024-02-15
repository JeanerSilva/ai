import openai
from secret import apikey
openai.api_key = apikey
from helpers import *


def obter_resposta_subtopicos(subtópico):
    messages_resposta = [
        {"role": "system", "content": "Você é um assistente que explica subtópicos em detalhes de modo a prover uma pessoa que fará concurso público"},
        {"role": "user", "content": f"fale informações importantes sobre o seguinte subtópico: {subtópico}. Se forem citados tipos, subtipos, classificações, tendências ou grupos, fale detidamente sobre cada um deles e cite exemplos."}
    ]
    response_resposta = openai.ChatCompletion.create(
        #model="gpt-4",
        model="gpt-3.5-turbo",
        messages=messages_resposta,
        temperature=0.1,
        max_tokens=500,
        frequency_penalty=1.0
    )
    
    return response_resposta['choices'][0]['message']['content'].strip()

def gerar_subtopicos_e_perguntas(pergunta, contexto):
    try:
        messages = [
            {"role": "system", "content": "Você é um assistente que gera subtópicos a partir de tópicos. Os subtópicos são os mais relevantes para elaboração de questões de concursos"},
            {"role": "user", "content": f"Dado o seguinte tema: '{pergunta.strip()}', liste importantes tópicos e subtópicos relacionados. A resposta deve vir no formato de tópicos e subtópicos separando os tópicos por ponto-e-vírgula"}
        ]

        response_subtopicos = openai.ChatCompletion.create(
            #model="gpt-3.5-turbo",  
            #model="gpt-3.5-turbo",
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.1,
            max_tokens=1024,
        )

        last_response = response_subtopicos['choices'][0]['message']['content']
        subtópicos = last_response.strip().split('\n')
        informacoes_subtopicos = []

        print(f"subtópicos======: {subtópicos} ")

        topico = ""
        pergunta = ""        
        for subtópico in subtópicos:
            if subtópico:
                if ehTopico(subtópico):
                    if pergunta == "":
                        topico = subtópico
                        print(f"adicionando: {topico} ao subtópico")
                        pergunta = topico                                        
                    else:                    
                        #resposta_subtópico = obter_resposta_subtopicos(pergunta)
                        print(f"pergunta: {pergunta}+++\n")
                        resposta_subtópico = pergunta
                        #print(f"resposta_subtópico: {resposta_subtópico}+++\n\n")
                        informacoes_subtopicos.append((subtópico, resposta_subtópico))
                        pergunta = ""
                else:
                    pergunta = pergunta + subtópico


        return informacoes_subtopicos
    except Exception as e:
        print(f"Erro ao gerar subtopicos e perguntas: {e}")
        return []

def ehTopico(string):
    num_pontos = string.count('.', 0, string[5:].find(' '))
    if num_pontos == 1:
        return True
    else:
        return False


def processar_perguntas(nome_arquivo, contexto):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        perguntas = arquivo.readlines()

    for pergunta in perguntas:
        arquivo =  sanitize_filename(pergunta[:-2]) + ".txt"
        with open("respostas/" + arquivo, 'a', encoding='utf-8') as arquivo_respostas:
            informacoes_subtopicos = gerar_subtopicos_e_perguntas(pergunta, contexto)

            print(f"informacoes_subtopicos {informacoes_subtopicos}")

            arquivo_respostas.write(f"Item do edital: {pergunta} \n")
            for i, (subtópico, resposta_subtópico) in enumerate(informacoes_subtopicos, start=1):
                arquivo_respostas.write(f"{i}. {subtópico}\n{resposta_subtópico}\n")
            arquivo_respostas.write("\n")

contexto = carrega("contexto.txt")

processar_perguntas('perguntas.txt', contexto)

