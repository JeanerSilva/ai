import re

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def sanitize_filename(filename):
    # Lista de caracteres proibidos no Windows e UNIX
    forbidden_chars = r'[<>:"/\\|?*\x00]'
    # Substitui os caracteres proibidos por nada (os remove)
    sanitized = re.sub(forbidden_chars, '', filename)
    # Remove espaços no final, que também podem causar problemas
    sanitized = sanitized.rstrip('. ')
    return sanitized