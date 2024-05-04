import re

def convert_latex_to_text(latex):
    def handle_frac(match):
        numerator, denominator = match.group(1), match.group(2)
        return f"{numerator} dividido por {denominator}"
    
    # Limpa os delimitadores de bloco LaTeX
    cleaned_latex = re.sub(r'\\\[|\]', '', latex)

    # Realiza substituições específicas para LaTeX
    cleaned_latex = re.sub(r'\\frac{(.+?)}{(.+?)}', handle_frac, cleaned_latex)
    cleaned_latex = re.sub(r'\\sqrt{(.+?)}', r'raiz quadrada de \1', cleaned_latex)
    cleaned_latex = cleaned_latex.replace(r'\times', ' vezes ')
    cleaned_latex = cleaned_latex.replace(r'\cdot', ' vezes ')
    cleaned_latex = cleaned_latex.replace(r'\sum', ' soma de ')
    cleaned_latex = cleaned_latex.replace(r'\int', ' integral de ')
    cleaned_latex = cleaned_latex.replace('-', ' menos ')  # Trata a subtração

    # Substituições para subscritos e superscritos
    #cleaned_latex = re.sub(r'_{(.+?)}', r' subscrito \1', cleaned_latex)
    cleaned_latex = re.sub(r'\^{(.+?)}', r' elevado a \1', cleaned_latex)

    # Remove chaves e barras invertidas restantes
    cleaned_latex = re.sub(r'[{}\\]', '', cleaned_latex)

    return cleaned_latex

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Encontra expressões LaTeX
    latex_expressions = re.findall(r'\\\[.*?\\\]', content, re.DOTALL)

    for latex in latex_expressions:
        text = convert_latex_to_text(latex)
        content = content.replace(latex, text)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Caminhos dos arquivos de entrada e saída
input_path = 'respostas/ipea_full.txt'
output_path = 'respostas/ipea_full_latex.txt'

# Processar o arquivo
process_file(input_path, output_path)
