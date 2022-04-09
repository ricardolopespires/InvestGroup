from django.shortcuts import render, get_object_or_404
import fundamentus
import json
from .models import Empresa, Setore, SubSetore
# Create your views here.


def setores(request):
    setores = Setore.objects.all()
    return render(request, "ações/setores/index.html", {'setores':setores} )


def setor(request, pk):
    setor = get_object_or_404(Setore, id = pk)
    empresa = Setore.objects.filter(nome = setor)
    return render(request, "ações/setores/setor.html",{'setor':setor})




def search(request): 
    query  = request.GET.get('search', None)
    print(query)

    if query :              
        papel = fundamentus.get_papel(query)
        result = papel.to_json(orient="records")
        search = json.loads(result)       
        return render(request, 'ações/search/index.html',{"search": search})

    return render(request, 'ações/search/index.html')



def details(request, papel):
    if Empresa.objects.filter(id = papel).exists():
        acoes_data = Empresa.objects.get(id = papel)
        empresa = get_object_or_404(Empresa, id = papel)
        our_db = True


        return render(request, "ações/details.html", {'empresa':empresa,'acoes_data ':acoes_data, 'our_db':our_db })

    else:

        papel = fundamentus.get_papel(papel)
        result = papel.to_json(orient="records")
        acoes_data = json.loads(result)




        setor_objs = []
        sub_setor_objs = []
        
		
        #Para os Setor        
        for setor in acoes_data: 
            try:
                a, created = Setore.objects.get_or_create(nome=setor['Setor'])
                setor_objs.append(a)
            except:
                pass

       
        
        for subsetor in acoes_data:
            print(subsetor['Subsetor']) 
            try:
                a, created = SubSetore.objects.get_or_create(nome=subsetor['Subsetor'])
                sub_setor_objs.append(a)
            except:
                pass

        for acoes_data in acoes_data:

            if acoes_data['EV_EBITDA'] == "-":
                EV_EBITDA = 0
            else:
                EV_EBITDA = acoes_data['EV_EBITDA']

            if acoes_data['EV_EBIT'] == "-":
                EV_EBIT = 0
            else:
                EV_EBIT = acoes_data['EV_EBIT'] 
                
            if acoes_data['Giro_Ativos'] == "-":
                Giro_Ativos = 0
            else:
                Giro_Ativos = acoes_data['Giro_Ativos']


            if  acoes_data['PEBIT'] == "-":
                PEBIT = 0
            else:
                PEBIT = acoes_data['PEBIT']

            if acoes_data['PSR'] == "-":
                PSR = 0
            else:
                PSR = acoes_data['PSR'] 
            
            m, created = Empresa.objects.get_or_create(
                
                id = acoes_data['Papel'], 
                Tipo = acoes_data['Tipo'],
                Empresa = acoes_data['Empresa'],
                img = "" ,           
                Cotacao =acoes_data['Cotacao'],
                Data_ult_cot = acoes_data['Data_ult_cot'],
                Min_52_sem = acoes_data['Min_52_sem'],
                Max_52_sem = acoes_data['Max_52_sem'],
                Vol_med_2m  = acoes_data['Vol_med_2m'],
                Valor_de_mercado = acoes_data['Valor_de_mercado'],
                Valor_da_firma = acoes_data['Valor_da_firma'],
                Ult_balanco_processado = acoes_data['Ult_balanco_processado'],
                Nro_Acoes = acoes_data['Nro_Acoes'],
                PL 	= acoes_data['PL'],
                PVP = acoes_data['PVP'],
                PEBIT =  PEBIT,
                PSR = PSR,
                PAtivos = acoes_data['PAtivos'],
                PCap_Giro = acoes_data['PCap_Giro'],
                PAtiv_Circ_Liq  = acoes_data['PAtiv_Circ_Liq'],
                Div_Yield = acoes_data['Div_Yield'],
                EV_EBITDA  = EV_EBITDA,
                EV_EBIT = EV_EBIT,
                Cres_Rec_5a = acoes_data['Cres_Rec_5a'],
                LPA = acoes_data['LPA'],
                VPA = acoes_data['VPA'],
                Marg_Bruta = acoes_data['Marg_Bruta'] ,
                Marg_EBIT = acoes_data['Marg_EBIT'] ,
                Marg_Liquida = acoes_data['Marg_Liquida'],
                EBIT_Ativo = acoes_data['EBIT_Ativo'],
                ROIC = acoes_data['ROIC'],
                ROE = acoes_data['ROE'],
                Liquidez_Corr = acoes_data['Liquidez_Corr'],
                Div_Br_Patrim = acoes_data['Div_Br_Patrim'],
                Giro_Ativos  = Giro_Ativos,
                Ativo = acoes_data['Ativo'],
                Disponibilidades = acoes_data['Disponibilidades'],
                Ativo_Circulante = acoes_data['Ativo_Circulante'],
                Div_Bruta = acoes_data['Div_Bruta'],
                Div_Liquida = acoes_data['Div_Liquida'],
                Patrim_Liq = acoes_data['Patrim_Liq'],
                Receita_Liquida_12m = acoes_data['Receita_Liquida_12m'],
                EBIT_12m = acoes_data['EBIT_12m'],
                Lucro_Liquido_12m = acoes_data['Lucro_Liquido_12m'],
                Receita_Liquida_3m = acoes_data['Receita_Liquida_3m'],
                EBIT_3m = acoes_data['EBIT_3m'],
                Lucro_Liquido_3m = acoes_data['Lucro_Liquido_3m'],
                )

            m.Setor.set(setor_objs)
            m.Sub_Setor.set(sub_setor_objs)


        
        for setor in setor_objs:            
            setor.empresas_setor.add(m)                   
            setor.save()

        for subsetor in sub_setor_objs:
            subsetor.empresas_sub_setor.add(m)        
            subsetor.save()


    m.save()
    our_db = False



    return render(request, "ações/details.html", {'acoes_data':acoes_data, 'our_db':our_db })