from django.views.generic import View, ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from quiz.models import Question, Answer, UsersAnswer
from django.db.models import Avg, Count, Sum ,F, Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Perfil, Situacao
from django.http import JsonResponse
from django.shortcuts import render
from accounts.models import User
from uuid import uuid4


# Create your views here.





#-------------------------------------- API Quiz---------- --------------------------------------------



class Situacao_Api_List(LoginRequiredMixin, View):
    

    def get(self, request):

        user = request.user.id

        if request.method == "GET":
            try:
                questions = []

                for question in Question.objects.filter(quiz_id = '7d03dbad-b6fd-40dc-8b91-269d9458d75f'):
                    

                    a = {

                        'user':user,'question': question.label, 'question_id':question.id,
                        'choice1':" ",'choice1_id':"", 'choice2':" ", 'choice2_id':"",
                        "choice3":" ","choice3_id":"",'A':" ",'B':" ", 'C':" ",

                      }

                    for answer in Answer.objects.filter(question_id = question.id):
                        answer
                        if answer.order == 1:
                            a['choice1'] = answer.label
                            a['choice1_id'] = answer.id
                            a['A'] = answer.score 
                        elif answer.order == 2:
                            a['choice2'] = answer.label
                            a['choice2_id'] = answer.id
                            a['B'] = answer.score  
                        elif answer.order == 3:
                            a['choice3'] = answer.label
                            a['choice3_id'] = answer.id
                            a['C'] = answer.score 

                    questions.append(a) 
                    
                    


                return JsonResponse({"questions": questions})
            except:
                return JsonResponse({"status": 1})







class Perfil_Api_List(LoginRequiredMixin, View):
    

    def get(self, request):

        user = request.user.id

        if request.method == "GET":
            try:
                questions = []

                for question in Question.objects.filter(quiz_id = '9140f723-46ae-4473-81d1-387ce66926ba'):
                    

                    a = {

                        'user':user,
                        'question': question.label,
                        'question_id':question.id,
                        'choice1':" ",
                        'choice1_id':"",
                        'choice2':" ",
                        'choice2_id':"",
                        "choice3":" ",
                        "choice3_id":"",
                        "choice4":" ",
                        "choice4_id":"",
                        'A':" ",
                        'B':" ",
                        'C':" ",
                        'D':" ",

                      }

                    for answer in Answer.objects.filter(question_id = question.id):
                        answer
                        if answer.order == 1:
                            a['choice1'] = answer.label
                            a['choice1_id'] = answer.id
                            a['A'] = answer.score 
                        elif answer.order == 2:
                            a['choice2'] = answer.label
                            a['choice2_id'] = answer.id
                            a['B'] = answer.score  
                        elif answer.order == 3:
                            a['choice3'] = answer.label
                            a['choice3_id'] = answer.id
                            a['C'] = answer.score
                        elif answer.order == 4:
                            a['choice4'] = answer.label
                            a['choice4_id'] = answer.id
                            a['D'] = answer.score 

                    questions.append(a) 
                    
                    


                return JsonResponse({"questions": questions})
            except:
                return JsonResponse({"status": 1})



@api_view(['GET'])
def AnswerList(request):
    answers = UsersAnswer.objects.all().order_by('-id')
    serializer = UsersAnswerListSerializer(answers, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def  AnswerCreate(request):
    serializer = UsersAnswerListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)




#-------------------------------------- API User Situação ------------------------------------------------------

@api_view(['GET'])
def situacaoList(request):
    situacoes = Situacao.objects.all().order_by('-id')
    serializer = SituacaoUserSerialiser(situacoes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def situacaoDetail(request, pk):
    situacaos = Situacao.objects.get(id = pk)
    serializer = SituacaoUserSerialiser(situacaos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def  situacaoCreate(request):
    serializer = SituacaoUserSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    


@api_view(['POST'])
def situacaoUpdate(request, pk):
    situacoes = Situacao.objects.get(id = pk)
    
    serializer = SituacaoUserSerialiser(instance = situacoes, data = request.data)

    if serializer.is_valid():
        print("esta ok")
        serializer.save()

    return Response(serializer.data)




#-------------------------------------- API User Situação ------------------------------------------------------

@api_view(['GET'])
def perfilList(request):
    situacoes = Perfil.objects.all().order_by('-id')
    serializer = PerfilUserSerialiser(situacoes, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def perfilDetail(request, pk):
    perfis = Perfil.objects.get(id = pk)
    serializer = PerfilUserSerialiser(perfis, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def  perfilCreate(request):
    serializer = PerfilUserSerialiser(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    


@api_view(['POST'])
def perfilUpdate(request, pk):
    perfis = Perfil.objects.get(id = pk)

    print(perfis)
    serializer = PerfilUserSerialiser(instance = perfis, data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def perfilDelete(request, pk):
    perfis = Perfil.objects.get(id = pk)
    serializer = PerfilUserSerialiser(instance = perfis, data = request.data)

    if serializer.is_valid():
        serializer.delete()

    return Response({'message': 'O Perfil foi excluído com sucesso!'}, status = status.HTTP_204_NO_CONTENT)


