import re
from django.core.exceptions import ValidationError

def validate_cpf(value):
    # Remove apenas os dígitos do CPF, ignorando os caracteres especiais
    numeros = [int(digito) for digito in value if digito.isdigit()]
    
    formatacao = False
    quant_digitos = False
    validacao1 = False
    validacao2 = False
    mensagem = "CPF inválido."

    # Verifica a estrutura do CPF (111.222.333-44)
    if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', value):
        formatacao = True

    if len(numeros) == 11:
        quant_digitos = True
        
        soma_produtos = sum(a*b for a, b in zip(numeros[0:9], range(10, 1, -1)))
        digito_esperado = (soma_produtos * 10 % 11) % 10
        if numeros[9] == digito_esperado:
            validacao1 = True

        soma_produtos1 = sum(a*b for a, b in zip(numeros[0:10], range(11, 1, -1)))
        digito_esperado1 = (soma_produtos1 * 10 % 11) % 10
        if numeros[10] == digito_esperado1:
            validacao2 = True

    if formatacao and quant_digitos and validacao1 and validacao2:
        return {"status": True, "mensagem": f"O CPF {value} é válido."}
    else:
        if not formatacao:
            mensagem = "O CPF está no formato incorreto. O formato correto é XXX.XXX.XXX-XX."
        elif not quant_digitos:
            mensagem = "O CPF deve conter 11 dígitos numéricos."
        elif not validacao1 or not validacao2:
            mensagem = "Os dígitos verificadores do CPF estão incorretos."
        
        return {"status": False, "mensagem": mensagem}


