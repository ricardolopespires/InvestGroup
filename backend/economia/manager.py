from django.shortcuts import render, get_object_or_404
from .models import  Continent, Currencie, Countrie
from rest_framework.response import Response
from rest_framework import status
from googletrans import Translator
from django.urls import reverse



import requests



class Economia:
    def __init__(self):
        self.transacoes = []

    def criar_favorito(self, query):

        url = "https://restcountries.com/v3.1/alpha/"+str(query["countries"])
        #url = "https://restcountries.com/v3.1/all"
        
        resp = requests.get(url)
        status = str(requests.get(url))

        dados = resp.json()
        if resp.status_code == 404:
            return Response({'message':'O Nome do país esta errado'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            #print(json.dumps(dados, indent=4, sort_keys=True, ensure_ascii=False))
            #qts  = len([x for x in dados[0]['borders']])
            id = dados[0]['cca2']
            name = dados[0]['name']['common']
            official = dados[0]['name']['official']
            area = dados[0]['area']
            try:
                borders = [x for x in dados[0]['borders']]
            except:
                borders = 'não adicionadas'
            
            capital = dados[0]['capital'][0]
            continents = dados[0]['subregion']
            population = dados[0]['population']
            coatOfArms = dados[0]['coatOfArms']['png']
            idioma = [x for x in dados[0]['languages'].keys()][0]
            languages =	dados[0]['languages'][idioma]
            moeda = [x for x in dados[0]['currencies'].keys()][0]
            flags = dados[0]['flags']['png']
            
            if Continent.objects.filter(subregion = dados[0]['subregion']).exists():
                pass
            
            else:
                cont, created = Continent.objects.get_or_create(
                    id = dados[0]['subregion'],
                    region = dados[0]['region'],
                    subregion = dados[0]['subregion']
                    )
                
            continent = get_object_or_404(Continent, subregion = continents)
            
            if Countrie.objects.filter(name = name.title()).exists():
                pass
            else:
                c, created = Countrie.objects.get_or_create(
                    id = dados[0]['cca2'],
					name = name,
					official = official,
					area = area,
					borders = borders,
					capital = capital,
					continents_id = continent.id,
					population = population,
					coatOfArms = coatOfArms,
					languages = languages,
					flags = flags,
					)
                
                c.user.add(query["user_id"])
            
            moeda = [x for x in dados[0]['currencies'].keys()][0]
            currencies = dados[0]['currencies'][moeda]
            
            if Currencie.objects.filter(name = currencies['name']).exists():
                currency = get_object_or_404(Currencie, name = currencies['name'])
            else :
                m, created =  Currencie.objects.get_or_create(
                    id = moeda,
					name = currencies['name'],
					symbol = currencies['symbol'],
					)
                
                pais = get_object_or_404(Countrie, name = name)
                m.paises.add(pais)
                m.save()

                moeda = get_object_or_404(Currencie, name = m)
                pais.currencies.add(moeda)
                pais.save()
                
            return Response({'success':True, 'message':"password reset is succesful"}, status=status.HTTP_201_CREATED)



    def ler_transacoes(self):
        for transacao in self.transacoes:
            print(f"Descrição: {transacao['descricao']}, Valor: {transacao['valor']}")

    def atualizar_transacao(self, indice, descricao, valor):
        if indice < len(self.transacoes):
            self.transacoes[indice] = {"descricao": descricao, "valor": valor}
        else:
            print("Índice inválido.")

    def deletar_transacao(self, indice):
        if indice < len(self.transacoes):
            del self.transacoes[indice]
        else:
            print("Índice inválido.")