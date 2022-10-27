from django.db.models import Avg, Count, Sum ,F, Q
from django.shortcuts import get_object_or_404
from googletrans import Translator
from .models import Calendario
from datetime import datetime
from uuid import uuid4
from datetime import date
import investpy



data_atual = date.today()
translator = Translator()



def calendario_economico():

    contador = 0
    while (contador < int(calendario.index.stop) ):

        calendario_id = calendario.iloc[contador].id
        if str(calendario.iloc[contador].time) == 'Tentative':
            time = ' 00:00'
        else:
            time = calendario.iloc[contador].time

        data = datetime.strptime(str(calendario.iloc[contador].date).replace('/','-') , '%d-%m-%Y')       
        zone = calendario.iloc[contador].zone
        currency = calendario.iloc[contador].currency
        importance = calendario.iloc[contador].importance
        event = calendario.iloc[contador].event
        actual = str(calendario.iloc[contador].actual).replace('None','0')
        forecast = str(calendario.iloc[contador].forecast).replace('None','0')
        previous = str(calendario.iloc[contador].previous).replace('None','0')


        if actual[-1] == 'K':
            K = True
        else:
            K = False


        if actual[-1] == 'M':
            M = True
        else:
            M = False

        if actual[-1] == 'B':
            B = True

        else:
            B = False

        if actual[-1] == '%':
            percent = True
        else:
            False
        
        actual   = actual.replace('K','')
        forecast = forecast.replace('K','')
        previous = previous.replace('K','')

      
        actual   = actual.replace('M','')
        forecast = forecast.replace('M','')
        previous = previous.replace('M','')

        
        actual   = actual.replace('B','')
        forecast = forecast.replace('B','')
        previous = previous.replace('B','')

        actual   = actual.replace('T','')
        forecast = forecast.replace('T','')
        previous = previous.replace('T','')

        
        actual   = actual.replace('%','')
        forecast = forecast.replace('%','')
        previous = previous.replace('%','')

        actual   = actual.replace(',','')
        forecast = forecast.replace(',','')
        previous = previous.replace(',','')

        actual   = float(actual)
        forecast = float(forecast)
        previous = float(previous)

        if actual == '0':
            actual = float(actual)

        elif forecast == '0':
            forecast = float(forecast)

        elif previous == '0':
            previous = float(previous)
        


        if Calendario.objects.filter(Q(id = calendario_id), Q(data__day = data_atual.day), Q(data__month = data_atual.month), Q(data__year = data_atual.year)).exists():
            
            evento = get_object_or_404(Calendario, id = calendario_id)                        
            evento.actual = actual
            evento.forecast = forecast
            evento.previous = previous
            evento.save()

        elif currency == None:
            pass

        else:
            Calendario.objects.get_or_create(


                id = uuid4(),
                codigo =  calendario_id,
                data = data,
                horario = time,
                pais = zone,
                moeda = currency,
                importancia = importance,
                evento = event,
                actual = actual,
                forecast = forecast,
                previous= previous,
                K = K,
                M = M,
                B = B,
                percent = False,
            )

        contador   = contador + 1
