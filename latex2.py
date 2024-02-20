import re

# Função para converter LaTeX para texto
def convert_latex_to_text(latex):
    def handle_frac(match):
        numerator, denominator = match.group(1), match.group(2)
        return f"{numerator} dividido por {denominator}"
    
    cleaned_latex = re.sub(r'\\\[|\]', '', latex)
    cleaned_latex = re.sub(r'\\frac{(.+?)}{(.+?)}', handle_frac, cleaned_latex)
    cleaned_latex = re.sub(r'\\(sqrt|times|cdot|sum|int)', '', cleaned_latex)
    cleaned_latex = re.sub(r'_{([^}]+)}', r' \1', cleaned_latex)
    cleaned_latex = re.sub(r'\^{([^}]+)}', r' elevado a \1', cleaned_latex)
    cleaned_latex = re.sub(r'[{}]', '', cleaned_latex)

    return cleaned_latex

# Função para processar o arquivo
def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Esta expressão regular procura por blocos de LaTeX, ajuste conforme necessário
    latex_expressions = re.findall(r'\\\[.*?\\\]', content, re.DOTALL)

    for latex in latex_expressions:
        text = convert_latex_to_text(latex)
        content = content.replace(latex, text)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Caminhos dos arquivos de entrada e saída
input_path = 'respostas/ipea.txt'
output_path = 'respostas/ipea_latex.txt'

# Processar o arquivo
process_file(input_path, output_path)
