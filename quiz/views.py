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

    def get(self, request):
        
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

    def get(self, request):

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

            name = request.POST.get('title')
            subjects = request.POST.get('subject')

            
            quiz = get_object_or_404(Quiz, id = question_id)


            
            #fazendo a atualização
            quiz.name = name           
            quiz.save()

            messages.success(request, 'Parabéns, A questão foi atualizada no banco de dados')
            return HttpResponseRedirect(reverse('quiz:list_questions', args  = [ question_id]))




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
        
        quiz = get_object_or_404(Quiz, id = question_id)
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





class Question_Updated_View(LoginRequiredMixin, View):

    def get(self, request, question_id):

      
        
        question = get_object_or_404(Question, id = question_id)
        quiz = get_object_or_404(Quiz, id=  question.quiz.id )       


        return render(request, 'quiz/management/questions/updated.html',{                    
           
            'question':question,
            'quiz':quiz,

            })


    def post(self, request, question_id):

        question = get_object_or_404(Question, id = question_id)
        quiz = get_object_or_404(Quiz, id=  question.quiz.id )

        if request.method == 'POST' :

            name = request.POST.get('label')

            print(name)


            Question.objects.filter(id = question.id).update(                        
                        
                        label =  name,                       

                        )

            messages.success(request, 'Parabéns, A questão foi atualizada no banco de dados')
            return HttpResponseRedirect(reverse('quiz:list_questions', args  = [ quiz.id ]))




class Delete_Question_View(LoginRequiredMixin, View):

    def get(self, request, question_id):      
            
        question = get_object_or_404(Question, id = question_id)
        quiz = get_object_or_404(Quiz, id=  question.quiz.id )


        return render(request, 'quiz/management/questions/delete.html',{

                    
            'quiz':quiz,
            'question':question,


            })


    def post(self, request, question_id):

        question = get_object_or_404(Question, id = question_id)
        quiz = get_object_or_404(Quiz, id=  question.quiz.id )

        question.delete()

        messages.success(request, 'Parabéns, A questão foi excluida no banco de dados')
        return HttpResponseRedirect(reverse('quiz:list_questions', args  = [ quiz.id ]))





class Answer_List_View(LoginRequiredMixin, View):


    def get(self, request,pk):

        
        question = get_object_or_404(Question, id =pk)
        answers = Answer.objects.filter(question_id =pk)
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
            score = request.POST.get('score')
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
                    score = score,
                    
                    )

                #contabilizando a quantidade das repostas
                answers.order = order + 1
                answers.save()               
                
                question.answers = order + 1
                question.save()

                messages.success(request, 'Parabéns, A nova questão já foi adicionada no banco de dados')
                return HttpResponseRedirect(reverse('quiz:answer_list', args  = [ question_id ]))



class Answer_Updated_View(LoginRequiredMixin, View):


    def get(self, request, question_id):
       
        
        answer = get_object_or_404(Answer, id = question_id)
        question = get_object_or_404(Question, id = answer.question.id)


        return render(request, 'quiz/management/questions/answer/updated.html',{

            'question':question,
            'answer':answer,                        
            })



    def post(self, request, question_id):

        answer = get_object_or_404(Answer, id = question_id)
        question = get_object_or_404(Question, id = answer.question.id)

        if request.method == 'POST':

            name = request.POST.get('name')
            score = request.POST.get('score')            
            

            Answer.objects.filter(id = question_id).update(

                label = name,
                score = score,
            )

            messages.success(request, 'Parabéns, A resposta foi atualizada no banco de dados com sucesso')
            return HttpResponseRedirect(reverse('quiz:answer_list', args  = [ question.id ]))





class Answer_Delete_View(LoginRequiredMixin, View):


    def get(self, request, question_id):
       
        question = get_object_or_404(Question, id = question_id)
        for answer in Answer.objects.filter( question_id = question.id):
            answer


        return render(request, 'quiz/management/questions/answer/delete.html',{

            'question':question,
            'answer':answer,                        
            })



    def post(self, request, question_id):

        if request.method == 'POST':

            question = get_object_or_404(Question, id = question_id)
            for answer in Answer.objects.filter( question_id = question.id):
                answer           
            

            answer.delete()

            messages.success(request, 'Parabéns, A resposta foi excluida no banco de dados')
            return HttpResponseRedirect(reverse('quiz:answer_list', args  = [ question_id ]))



     
     
#--------------------------------------------- API  ----------------------------------------------------

