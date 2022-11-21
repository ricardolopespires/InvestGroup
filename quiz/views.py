from .api import QuestionListSerializer, UsersAnswerListSerializer, UsersAnsweraDetailSerializer
from django.views.generic import View, ListView, TemplateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quiz, Question, Answer, UsersAnswer
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count, Sum ,F, Q
from django.shortcuts import redirect, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from django.utils.text import slugify
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, datetime
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from accounts.models import User
from uuid import uuid4







#---------------------------------------- PROFILE ----------------------------------------------------


class Profile_View(LoginRequiredMixin, View):

    def get(self, request, usuario_id):
        return render(request, 'profile/index.html')



class Profile_Perfil_Investor(LoginRequiredMixin,View):

    def get(self, request, usuario_id):
        usuario = get_object_or_404(User, id = usuario_id)
        quiz = Quiz.objects.all()
        questions = Question.objects.all()

        return render(request, 'quiz/dashboard/perfil/index.html',{

            'quiz':quiz,
            'questions':questions,

            })

    def post(self, request, usuario_id):
        usuario = get_object_or_404(User, id = usuario_id)

        count = 0

        if request.method == 'POST':

            questions = request.POST.getlist('question')
            
            for questao in questions:
                resposta = get_object_or_404(Question, id = questao)
                count += resposta.valor

            print(count)
            for perfil in Perfil.objects.all():

                if count in range(perfil.minimum, perfil.maximum):                    
                    user.perfil = perfil.investor
                    user.save()



                

            return HttpResponseRedirect(reverse('quiz:perfil_investidor', args=[usuario.id]))





class Profile_Financial_Situation(LoginRequiredMixin, View):



    def get(self, request, usuario_id):

        return render(request, 'quiz/dashboard/situation/index.html')


class List_Quiz_View(LoginRequiredMixin, View):


    def get(self, request):

        
        quizzes = Quiz.objects.all()
        
        return render(request, 'quiz/management/list.html', {
            
            'quizzes':quizzes,

             })



class Created_Quiz_View(LoginRequiredMixin, View):

    def get(self, request):

        

        return render(request, 'quiz/management/created.html')



    def post(self, request):

        if request.method == 'POST':

                       
            order = Quiz.objects.all().count()
            name = request.POST.get('name')
            topico = request.POST.get('topico')
            description = request.POST.get('description') 
            


            if Quiz.objects.filter(name = name).exists():
                messages.info(request, 'Ops.... Essa questão já foi adicionada no banco de dados ')
                return HttpResponseRedirect(reverse('quiz:list_quiz'))
            else:

                quiz = Quiz(


                    id = uuid4(),
                    order = order,    
                    name = name,   
                    slug = slugify(name),
                    description = description,
                    created = date.today(),
                    topic = topico,
                    percentage = 0,
                    total = 0,
                    active = True,
                    timestamp = 0,                                 
                    
                   
                    )

                quiz.order = order + 1
                quiz.save()               
                
                messages.success(request, 'Parabéns, A novo questionário já foi adicionada no banco de dados')
                return HttpResponseRedirect(reverse('quiz:list_quiz'))



class Updated_Quiz_View(LoginRequiredMixin, View):

    def get(self, request, question_id):

        
        quiz = get_object_or_404(Quiz, id = question_id)

        return render(request, 'quiz/management/updated.html',{
            'quiz':quiz,          

            })



    def post(self, request, question_id):

        if request.method == 'POST':

            name = request.POST.get('name')
            subjects = request.POST.get('subject')

            
            quiz = get_object_or_404(Quiz, id = question_id)


            
            #fazendo a atualização
            quiz.name = name
            quiz.subject.add(subjects)
            quiz.save()

            messages.success(request, 'Parabéns, A questão foi atualizada no banco de dados')
            return HttpResponseRedirect(reverse('quiz:quiz_detail', args  = [ question_id]))




class Delete_Quiz_View(LoginRequiredMixin, View):

    def get(self, request, question_id):

       
        quiz = get_object_or_404(Quiz, id = question_id)

        return render(request, 'quiz/management/delete.html',{

            'quiz':quiz,
           
            })


    def post(self, request, question_id):

        quiz = get_object_or_404(Quiz, id = question_id)

        quiz.delete()

        messages.success(request, 'Parabéns, A questão foi excluida no banco de dados')
        return HttpResponseRedirect(reverse('quiz:quiz_detail', args  = [ question_id ]))





class Question_List_View(LoginRequiredMixin, View):


    def get(self, request, question_id):
        
        quiz = get_object_or_404(Quiz.objects, id = question_id)
        questions = Question.objects.filter(quiz_id = quiz.id)
        total = Question.objects.filter(quiz_id = quiz.id).count()

        if total > 2:
            quiz.questions = True
            quiz.save()


        return render(request, 'quiz/management/questions/list.html',{

            'quiz':quiz,            
            'questions':questions
            

            })





class Question_Created_View(LoginRequiredMixin, View):


    def get(self, request, question_id):
       
        quiz = get_object_or_404(Quiz, id = question_id)
        
        return render(request, 'quiz/management/questions/created.html',{ 'quiz':quiz })


    def post(self, request, question_id):

        
        quiz = get_object_or_404(Quiz, id = question_id)
        total = Question.objects.filter(quiz_id = quiz.id).count()

        if request.method == 'POST':

            name = request.POST.get('label')

            if Question.objects.filter(label = name).exists():
                messages.info(request, 'Ops.... Essa questão já foi adicionada no banco de dados ')
                return HttpResponseRedirect(reverse('quiz:list_questions', args  = [ question_id]))
            else:
                

                Question.objects.get_or_create(

                    id = uuid4(),
                    quiz_id = question_id, 
                    label =  name,
                    order =  total + 1,

                    )

                quiz.total += 1
                quiz.save()

                messages.success(request, 'Parabéns, A questão foi adicionado no banco de dados')
                return HttpResponseRedirect(reverse('quiz:list_questions', args  = [ question_id]))




            



class Delete_Question_View(LoginRequiredMixin, View):

    def get(self, request, quiz_id, question_id):

      
        question = get_object_or_404(Question, id = question_id)
        quiz = get_object_or_404(Quiz, id = quiz_id)




        return render(request, 'quiz/management/questions/delete.html',{

            'question':question,           
            'quiz':quiz,


            })


    def post(self, request, quiz_id, question_id):

        question = get_object_or_404(Question, id = question_id)

        question.delete()

        messages.success(request, 'Parabéns, A questão foi excluida no banco de dados')
        return HttpResponseRedirect(reverse('quiz:list_questions', args  = [ quiz_id ]))




class Answer_List_View(LoginRequiredMixin, View):


    def get(self, request, question_id):

        
        question = get_object_or_404(Question, id = question_id)
        answers = Answer.objects.filter(question_id = question_id)
        quiz = get_object_or_404(Quiz, id = question.quiz.id)

        

        return render(request, 'quiz/management/questions/answer/list.html',{

            'quiz':quiz,
            'question':question,
            'answers':answers,
            })


    




class Answer_Created_View(LoginRequiredMixin, View):


    def get(self, request, question_id):
       
        question = get_object_or_404(Question, id = question_id)

        
        return render(request, 'quiz/management/questions/answer/created.html',{

            'question':question,
                        
            })



    def post(self, request, question_id):

        if request.method == 'POST':

            name = request.POST.get('name')            
            order = Answer.objects.filter(question_id = question_id).count()
            question = get_object_or_404(Question, id = question_id)
            
            


            if Answer.objects.filter(label = name).exists():
                messages.info(request, 'Ops.... Essa resposta já foi adicionada no banco de dados ')
                return HttpResponseRedirect(reverse('quiz:answer_list', args  = [ question_id ]))
            else:

                answers = Answer(


                    id = uuid4(),                    
                    question_id = question_id, 
                    label = name,
                    order = order,
                    
                    )

                #contabilizando a quantidade das repostas
                answers.order = order + 1
                answers.save()               
                
                question.answers = order + 1
                question.save()

                messages.success(request, 'Parabéns, A nova questão já foi adicionada no banco de dados')
                return HttpResponseRedirect(reverse('quiz:answer_list', args  = [ question_id ]))



     



#--------------------------------------------- API  ----------------------------------------------------

class Question_Api_List(LoginRequiredMixin, View):
    

    def get(self, request):

        if request.method == "GET":
            try:
                questions = []

                for question in Question.objects.all():

                    a = {'question': question.label, 'choice1':" ", 'choice2':" ", "choice3":" ", 'A':" ",'B':" ", 'C':" ",}

                    for answer in Answer.objects.filter(question_id = question.id):
                        answer
                        if answer.order == 1:
                            a['choice1'] = answer.label
                            a['A'] = answer.score 
                        elif answer.order == 2:
                            a['choice2'] = answer.label
                            a['B'] = answer.score  
                        elif answer.order == 3:
                            a['choice3'] = answer.label
                            a['C'] = answer.score 

                    questions.append(a) 
                    
                    


                return JsonResponse({"questions": questions})
            except:
                return JsonResponse({"status": 1})




class Situacao_Question_Api(LoginRequiredMixin, View):


    def get(self, request):

        if request.method == 'GET':

            nome = request.GET.get('nome')
            email = request.GET.get('email')

            print(nome)
            print(email)

            return JsonResponse({'email':email})


    def post(self, request):


        if request.method == "POST":
            nome = request.POST.get('nome')
            email = request.POST.get('email')

            print(nome)
            print(email)

            return JsonResponse({'email':email})





class Question_User_View(LoginRequiredMixin, View):


    def get(sel, request):
        question = Question.objects.filter( id  = '3b02eae4-314a-413c-be2c-94377e6a8020')
        return render(request, 'quiz/dashboard/situation/list.html' )



class UsersAnswerAPIView(generics.ListAPIView):

    queryset = UsersAnswer.objects.all()
    serializer_class = UsersAnswerListSerializer



class UserAnswerRetrieveAPIView(generics.RetrieveAPIView):

    Lookup_field = 'id'
    queryset = UsersAnswer.objects.all()
    serializer_class = UsersAnsweraDetailSerializer 


class UserAnswerCreateAPIView(generics.CreateAPIView):
    queryset = UsersAnswer.objects.all()
    serializer_class = UsersAnsweraDetailSerializer 
