from urllib.request import urlopen
from bs4 import BeautifulSoup
from googletrans import Translator
from datetime import datetime, date
import os
from uuid import uuid4
import time


translator = Translator()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InvestGroup.settings")

import django
django.setup()


from django.shortcuts import render, redirect, get_object_or_404, reverse
from accounts.models import User, Questionnaire, Questions
from django.utils.text import slugify
import requests
import json



question = [{
    "QUESTÃO 02: Por quanto tempo pretende deixar seus recursos investidos":['1 - Até 1 ano.','2 - 1 a 5 anos.','3 - Mais de 5 anos.','4 - Essa reserva não será utilizada, a não ser em caso de emergência.'],
    'QUESTÃO 03: Em relação aos seus investimentos na SLW, qual é a necessidade futura dos recursos aplicados?':['1 - Preciso desse dinheiro como complemento de renda.','2 - Eventualmente posso precisar utilizar uma parte dele.','3 - Não tenho necessidade imediata desse dinheiro.'],
    'QUESTÃO 04: Qual a sua renda mensal?':['1 - Até R$ 3.000,00.','2 - Entre R$ 3.000,00 e R$ 5.000,00.','3 - Entre R$ 5.000,00 e R$ 10.000,00.','4 - Entre R$ 10.000,00 e R$ 30.000,00.','5 - Mais de R$ 30.000,00.',],
    'QUESTÃO 05: Qual percentual da sua renda o (a) Sr.(a) investe regularmente?':['1 - Até 10%.','2 - De 10 a 20%.','3 - De 20% a 50%.','4 - Acima de 50%.'],
    'QUESTÃO 06: Por conta de oscilações do mercado, considere que seus investimentos percam 10% do valor aplicado. Neste ':['1 - Não sei o que faria.','2 - Venderia toda a posição.','3 - Manteria a posição.','4 - Aumentaria a posição.'],
    'QUESTÃO 07: Quais dos produtos listados abaixo você tem familiaridade? (Esta questão permite múltiplas respostas. Para fins de cálculo de Perfil, deve ser utilizada a resposta de maior valor de pontuação entre as respostas assinaladas).':['1 - Poupança, Fundos DI, CDB, Fundos de Renda Fixa.','2 - Fundos Multimercados, Títulos Públicos, LCI, LCA.','3 - Fundos de Ações, Ações, Fundos Imobiliários, Debêntures, Fundos Cambiais, Clubes de Investimento.','4 - Fundos de Investimentos em Participações (FIP), Derivativos (Futuros, Opções e Swaps).',],
    'QUESTÃO 08: Quais investimentos você realizou frequentemente nos últimos 24 meses?':['1 - Nunca investi. Primeiro aporte.','2 - Investi apenas em produtos ou fundos de renda fixa.','3 - Investi em produtos ou fundos de renda fixa e/ ou de multimercado e/ou de renda variável e/ou com derivativos com finalidade de hedge.','4 - Investi em produtos de renda fixa e/ou de multimercado e/ou de renda variável e/ou com derivativos com finalidade de especulação ou alavancagem.',],
    'QUESTÃO 09: Qual é a atual composição dos seus investimentos por categoria? (Esta questão permite múltiplas respostas Para fins de cálculo do Perfil, deve ser utilizada a resposta com o maior percentual e no caso de respostas com porcentagens iguais, deve ser utilizada a resposta mais conservadora).':[
'1 - 0 á 10% Renda Variável (Ações e Fundos de Ações).','2 - 11 á 20% Renda Variável (Ações e Fundos de Ações).','3 - 21 á 40% Renda Variável (Ações e Fundos de Ações).','4 - 41 á 60% Renda Variável (Ações e Fundos de Ações).','5 - 61 á 100% Renda Variável (Ações e Fundos de Ações).','6 - 0 á 10% Fundos de Investimento Multimercado.','7 - 11 á 20% Fundos de Investimento Multimercado.','8 - 21 á 40% Fundos de Investimento Multimercado.','9 - 41 á 60% Fundos de Investimento Multimercado.','10 - 61 á 100% Fundos de Investimento Multimercado.','11 - 0 á 10% Renda Fixa (Fundos de Renda Fixa, DI, CDBs, Poupança).','12 - 11 á 20% Renda Fixa (Fundos de Renda Fixa, DI, CDBs, Poupança).','13 - 21 á 40% Renda Fixa (Fundos de Renda Fixa, DI, CDBs, Poupança).','14 - 41 á 60% Renda Fixa (Fundos de Renda Fixa, DI, CDBs, Poupança).','15 - 61 á 100% Renda Fixa (Fundos de Renda Fixa, DI, CDBs, Poupança).','16 - 0 á 10% Imóveis.','17 - 11 á 20% Imóveis.','18 -  21 ás 40% Imóveis.','19 - 40 á 60% Imóveis.','20 - 0 ás 10% Outros.','21 - 11 ás 20% Outros.','22 - 21 ás 40% Outros.','23 - 41 ás 60% Outros.','24 - 61 ás 100% Outros.',],
    'QUESTÃO 10: Qual é o valor do seu Patrimônio?':['1  Até R$ 10.000,00.','2 Entre R$ 10.000,01 e R$ 20.000,00.','3 Entre R$ 20.000,01 e R$ 50.000,00.','4 Entre R$ 50.000,01 e R$ 100.000,00.','5 Entre R$ 100.000,01 a R$ 500.000,00.','6 Entre R$ 500.000,01 a R$ 1.000.000,00.','7 Acima de R$ 1.000.000,01.',
],
    'QUESTÃO 11: Como você classificaria a relação de sua formação acadêmica e da sua experiência profissional em relação aos seus conhecimentos sobre o mercado financeiro?':[
'1 - Não tenho formação acadêmica na área financeira, mas desejo operar no mercado de capitais e financeiro.','2 - Apesar de não ter a formação acadêmica na área financeira possuo experiência no mercado de capitais e financeiro.','3 - Tenho formação na área financeira e conheço as regras do mercado financeiro.','4 - Tenho formação acadêmica e experiência profissional na área financeira, por isto conheço profundamente o mercado financeiro, como operações de derivativos e estruturadas.'],
    'QUESTÃO 12: Qual das respostas abaixo mais se assemelha à sua personalidade como investidor?':[
'1 - Não admito perder nada do capital investido. Procuro um retorno seguro e sem oscilações. Segurança é mais importante do que rentabilidade.','2 - Não admito perder nada do capital investido, no entanto posso arriscar uma parte do capital para alcançar resultados melhores que a renda fixa tradicional. Valorizo mais a segurança do que a rentabilidade.','3 - Posso correr riscos para conseguir uma rentabilidade acima da média, no entanto, prezo a preservação de 100% do capital investido. Divido minhas preferências entre segurança e rentabilidade, mas ainda prefiro segurança à rentabilidade.','4 - Admito perdas de até 20% do capital investido, se a proposta de investimento gerar possibilidade de altos retornos. A procura por rentabilidade é mais importante do que a segurança.','5 - Minha prioridade é maximizar a rentabilidade, com a segurança em segundo plano. Posso correr grande riscos para obter elevados retornos, admitindo perder mais de 20% do meu capital investido.'],
    


    }]

'''
for q in question:

    Questionnaire.objects.get_or_create(

        id = uuid4(),
        title = q,

        )

'''
for q in question:
    for keys,values in q.items():
        if Questionnaire.objects.filter(title = keys).exists():
            questionario = get_object_or_404(Questionnaire, title = keys)            
            print(questionario.id)
            for v in values:
                if Questions.objects.filter(answers = v).exists():
                    if Questions.objects.filter(questionnaire_id = '7d5e8132-23ac-40d2-a09f-45fb2553486a').exists():
                        for questao in Questions.objects.all():
                            questao.valor = 2
                            questao.save()
                        
                
                else:                    
                    Questions.objects.get_or_create(

                        id = uuid4(),
                        questionnaire_id = questionario.id,
                        answers = v,
                        correct = False,
                        valor = 0,
                        
                        )
































    

