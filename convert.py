from spire.doc import *
from spire.doc.common import *


def resume_diretorio(diretorio):
    arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.txt')]
    for nome_arquivo in arquivos:
        converte_arquivo(diretorio, nome_arquivo)    

def converte_arquivo(diretorio, nome_arquivo):
    document = Document()
    document.LoadFromFile(diretorio + nome_arquivo)

    pos_ultimo_ponto = nome_arquivo.rfind('.')
    nome_base = nome_arquivo[:pos_ultimo_ponto] if pos_ultimo_ponto != -1 else nome_arquivo
    
    document.SaveToFile(diretorio + nome_base + ".doc", FileFormat.Docx2016)
    document.Close()

resume_diretorio("respostas/")