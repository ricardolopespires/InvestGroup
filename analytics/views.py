from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Selic
from datetime import datetime
from datetime import date
import requests
import json
import pandas as pd
from .utils import get_plot


# Create your views here.






def selic(request):
    taxa_selic = Selic.objects.all().order_by('-data')
    qs = Selic.objects.all()
    
    paginator = Paginator(taxa_selic , 10) # 3 posts in each page
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)    
    '''    
    x = [x.data for x in qs]
    y = [y.taxa for y in qs]
    chart = get_plot(x,y)
    '''
    return render (request, 'analytics/selic.html',{'page': page, 'posts': posts,'taxa_selic':taxa_selic, 'qs':qs})


def updated_selic(request):

    selic = Selic.objects.all()
    date_new = Selic.objects.all().last()    
    
    dataInicial = date_new.data.strftime('%d-%m-%Y')
    dataFinal =  datetime.today().strftime('%d-%m-%Y')  

    tempo = abs((datetime.today() - pd.Timestamp(dataInicial))).days
 
    if tempo >= 7:

        url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial='+ str(dataInicial) + '&dataFinal='+ str(dataFinal)
        #url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json'
        response = requests.get(url)
        selic_data = response.json()


        for selic in selic_data:
            try:
                data = selic['data']
                data2 = datetime.strptime(data, "%d/%m/%Y")        

                _, create = Selic.objects.get_or_create(                      
                        data = data2,
                        taxa = selic['valor'],
                    )
                
                print(data2)
    
            except:
                pass
        
    else:
        print("A diferença entre a ultima atualização é {}, precisa de 7 para nova  atualização".format(tempo))   
    return HttpResponseRedirect(reverse( 'analytics:selic'))
