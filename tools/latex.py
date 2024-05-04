import re

def convert_latex_to_text(latex):
    # Função auxiliar para tratar frações
    def handle_frac(match):
        # Extrai numerador e denominador, considerando o conteúdo completo das chaves
        numerator, denominator = match.group(1), match.group(2)
        return f"{numerator} dividido por {denominator}"
    
    # Remove os delimitadores de bloco LaTeX
    cleaned_latex = re.sub(r'\\\[|\]', '', latex)

    # Substituição para a expressão de fração, usando a função auxiliar
    cleaned_latex = re.sub(r'\\frac{(.+?)}{(.+?)}', handle_frac, cleaned_latex)

    # Substituições gerais
    cleaned_latex = re.sub(r'\\(sqrt|times|cdot|sum|int)', '', cleaned_latex)
    cleaned_latex = re.sub(r'_{([^}]+)}', r' \1', cleaned_latex)  # Substitui subscritos
    cleaned_latex = re.sub(r'\^{([^}]+)}', r' elevado a \1', cleaned_latex)  # Substitui superscritos

    # Limpeza final
    cleaned_latex = re.sub(r'[{}]', '', cleaned_latex)  # Remove chaves restantes

    return cleaned_latex

# Exemplo de uso
latex_formula = r"\[ X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}} \]"
text = convert_latex_to_text(latex_formula)
print(text)
