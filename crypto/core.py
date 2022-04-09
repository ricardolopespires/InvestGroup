from django.shortcuts import get_object_or_404
import requests
import json





def porcentagem(valor_anterior, valor_atual):
    porcetagem = 100
    try:
        calculo = porcetagem / int(valor_anterior)
    except:
        calculo = porcetagem / 1
    resultado =  calculo * valor_atual 
    return round(resultado, 2)



def price_percentage_change(cripto_id,  datetime, timedelta ):

    p_30 =  (datetime.now() + timedelta(days= -30)).strftime('%d-%m-%Y')
    p_60 =  (datetime.now() + timedelta(days= -60)).strftime('%d-%m-%Y')
    p_180 =  (datetime.now() + timedelta(days= -180)).strftime('%d-%m-%Y')
    p_1 =  (datetime.now() + timedelta(days= -366)).strftime('%d-%m-%Y')



    def data_percentage(cripto_id, data):

        url = str("https://api.coingecko.com/api/v3/coins/"+str( cripto_id )+"/history?date="+str(data))    

        response = requests.get(url)
        data_crypto = response.json()
        
        return data_crypto['market_data']['current_price']['usd']
        

    #print(json.dumps( data_percentage(cripto_id, p_30), indent=4, sort_keys=True))
    #print( data_percentage(cripto_id, p_60 ))
    #print( data_percentage(cripto_id, p_180 ))
    #print( data_percentage(cripto_id, p_1 ))

    '''
    if dados.objects.filter( id = cripto_id ).exists():


        for data_cripto in data.objects.filter(id = cripto_id ):


            data_inicial = datetime.now().strftime('%y-%m-%d')
            data_final = str(data_cripto.periodo.strftime("%Y-%m-%d %H:%M:%S"))
            f = "%Y-%m-%d %H:%M:%S"
            
            inicio = datetime.strptime(data_inicial, f)
            fim = datetime.strptime(data_final, f)
            di = abs(relativedelta(inicio, fim))


        if di.days == 30:

            dados.objects.all().create(

                id = cripto_id,
                periodo = datetime.now().strftime('%y-%m-%d'),
                data = datetime.now().strftime('%y-%m-%d'),
                p_30 = data_percentage(cripto_id, p_30),
                p_90 = data_percentage(cripto_id, p_60 ),
                p_180 = data_percentage(cripto_id, p_180 ),
                p_1 = data_percentage(cripto_id, p_1 ),
            
            )
        else:

            Cripto.objects.filter( id = crypto['id']).update(

                id = cripto_id,
                #periodo = datetime.now().strftime('%y-%m-%d'),
                data = datetime.now().strftime('%y-%m-%d'),
                p_30 = data_percentage(cripto_id, p_30),
                p_90 = data_percentage(cripto_id, p_60 ),
                p_180 = data_percentage(cripto_id, p_180 ),
                p_1 = data_percentage(cripto_id, p_1 ),
                
                )

    else:
        dados.objects.all().create(

            id = cripto_id,
            periodo = datetime.now().strftime('%y-%m-%d'),
            data = datetime.now().strftime('%y-%m-%d'),
            p_30 = data_percentage(cripto_id, p_30),
            p_90 = data_percentage(cripto_id, p_60 ),
            p_180 = data_percentage(cripto_id, p_180 ),
            p_1 = data_percentage(cripto_id, p_1 ),
            
            )
    '''
    



def cripto_history(start, end):
    start = datetime.datetime.strptime("01-01-2022", "%d-%m-%Y")
    end = datetime.datetime.strptime("22-01-2022", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
    for date in date_generated: 
        data = cg.get_coin_history_by_id(id='ethereum',date = (date.strftime("%d-%m-%Y")), localization='false')
        print(data)



def retornos_acumalados(mensal):
    capital = 100
    retornos = []
    for r in mensal:
        capital += capital*r.total
        retornos.append(capital - 1)
    return retornos




def retorns_com_aportes(p_patrimonio, aporte):
    retorns = [0]
    for i in range(1, len(p_patrimonio )):
        retornos.append(( p_patrimonio[i] - aporte ) / p_patrimonio[i - 1] - 1)
    return retornos




