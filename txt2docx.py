
from docx import Document

def convert_txt_to_docx(txt_file_path, docx_file_path):
    # Criar um novo documento Word
    doc = Document()
    
    # Abrir o arquivo de texto e ler o conteúdo
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Adicionar cada linha como um parágrafo no documento Word
    for line in lines:
        doc.add_paragraph(line)
    
    # Salvar o documento Word
    doc.save(docx_file_path)

# Caminho do arquivo de texto de entrada
txt_file_path = "respostas/Realidade.txt"

# Caminho do arquivo Word de saída
docx_file_path = "respostas/Realidade.docx"

# Converter o arquivo txt em docx
convert_txt_to_docx(txt_file_path, docx_file_path)
