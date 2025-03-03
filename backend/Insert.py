import os
import sys
import django
import json  # Para lidar com o arquivo JSON

# Definindo a variável de ambiente para as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Inicializando o Django
django.setup()
from quiz.models import Quiz, Question, Answer 
from django.shortcuts import get_object_or_404
# Usando um gerenciador de contexto para abrir e ler o arquivo JSON com codificação UTF-8
try:
    with open("Situacao.json", "r", encoding="utf-8") as dataset:
        data = json.load(dataset)  # Carrega os dados do JSON para um objeto Python
except FileNotFoundError:
    print("Erro: O arquivo 'Perfil.json' não foi encontrado.")
    sys.exit(1)
except json.JSONDecodeError:
    print("Erro: O arquivo JSON está mal formatado.")
    sys.exit(1)

# Agora 'data' contém os dados do JSON, e você pode trabalhar com eles
formulario = data.get('formulario_situacao_financeira', {})



# Exibindo o título e as instruções
titulo = formulario.get('titulo', 'Título não disponível')
instrucoes = formulario.get('instrucoes', 'Instruções não disponíveis')

print(f"{titulo}\n")
print(f"Instruções: {instrucoes}\n")

count = 76

# Verificando se 'perguntas' existe e contém perguntas
if "perguntas" in formulario:
    for i, pergunta in enumerate(formulario["perguntas"], start=1):
        print(f"Pergunta {i}: {pergunta['pergunta']}")
        q, create = Question.objects.get_or_create(
            id = pergunta['id'],
            quiz_id = 2,
            title = pergunta['pergunta']
            )        
        
        # Exibindo as respostas e pontuações
        print(q.id)
        for j, resposta in enumerate(pergunta["respostas"], start=1):
            print(f"  {j}. {resposta['texto']} (Pontuação: {resposta['pontuacao']})")
        
            a, create = Answer.objects.get_or_create(
                id = count,
                question_id = q.id,
                answer_text = resposta['texto'],  
                is_right = True,
                score = resposta['pontuacao']                
                )
            count += 1
        
        print()  # Para adicionar uma linha em branco entre as perguntas
else:
    print("Nenhuma pergunta encontrada no formulário de perfil de investidor.")
