import openai

openai.api_key =='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'


from helpers import *


def obter_resposta_subtopicos(subtópico):
    messages_resposta = [
        {"role": "system", "content": "Você trabalha no CESPE/CEBRASPE e faz perguntas para concursos públicos."},
        {"role": "user", "content": f"Crie 10 afirmativas diretas e verdadeiras sobre: {subtópico}"}
    ]
    response_resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_resposta
    )
    return response_resposta['choices'][0]['message']['content'].strip()

def gerar_subtopicos_e_perguntas(pergunta, contexto):
    try:
        messages = [
            {"role": "system", "content": "Você é um assistente que gera subtópicos a parti de tópicos."},
            {"role": "user", "content": f"Dado o seguinte tema: '{pergunta.strip()}', liste os 10 mais importantes subtópicos relacionados."}
        ]

        temperature=0.1
        max_tokens=150
        frequency_penalty=1.0

        response_subtopicos = openai.ChatCompletion.create(
            #model="gpt-3.5-turbo",  
            model="gpt-4",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty

        )
        
        # Processar a resposta para extrair os subtópicos
        last_response = response_subtopicos['choices'][0]['message']['content']
        subtópicos = last_response.strip().split('\n')
        informacoes_subtopicos = []

        for subtópico in subtópicos:
            if subtópico:
                resposta_subtópico = obter_resposta_subtopicos(subtópico)
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
            arquivo_respostas.write(f"Pergunta Original: {pergunta} \n")
            for i, (subtópico, resposta_subtópico) in enumerate(informacoes_subtopicos, start=1):
                arquivo_respostas.write(f"{i}. Subtópico: \n{subtópico}\nAssertivas:\n {resposta_subtópico}\n\n")
            arquivo_respostas.write("\n")

contexto = carrega("contexto.txt")

processar_perguntas('perguntas.txt', contexto)
