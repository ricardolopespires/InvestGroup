from django.views.generic import View, ListView, TemplateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  Questionnaire, Questions, Perfil, Subject
from django.db.models import Avg, Count, Sum ,F, Q
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, datetime
from django.shortcuts import render
from accounts.models import User
from uuid import uuid4



#---------------------------------------- PROFILE ----------------------------------------------------


class Profile_View(LoginRequiredMixin, View):

    def get(self, request, usuario_id):
        return render(request, 'profile/index.html')



class Profile_Perfil_Investor(LoginRequiredMixin,View):

    def get(self, request, usuario_id):
        usuario = get_object_or_404(User, id = usuario_id)
        questionnaires = Questionnaire.objects.all()
        questions = Questions.objects.all()

        return render(request, 'quiz/dashboard/perfil/index.html',{

            'questionnaires':questionnaires,
            'questions':questions,

            })

    def post(self, request, usuario_id):
        usuario = get_object_or_404(User, id = usuario_id)

        count = 0

        if request.method == 'POST':

            questions = request.POST.getlist('question')
            
            for questao in questions:
                resposta = get_object_or_404(Questions, id = questao)
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
        subjects= Subject.objects.all() 
        usuarios = subjects.aggregate(total = Sum('usuario'))['total']
        
        return render(request, 'quiz/management/manager/index.html',{

            'subjects':subjects,
            'usuarios':usuarios,

            })


class Detail_Quiz_View(LoginRequiredMixin, View):


    def get(self, request, subject_id):

        subjects = get_object_or_404(Subject, id = subject_id)
        questionarios = Questionnaire.objects.filter(subject = subjects )
        

        if subjects.total > 0:
            subjects.total = questionarios.count()
            subjects.save()

        elif subjects.total != questionarios.count():
            subjects.total = questionarios.count()
            subjects.save()
        
        return render(request, 'quiz/management/manager/detail.html', {
            
            'subjects': subjects,
            'questionarios':questionarios,

             })



class Created_Quiz_View(LoginRequiredMixin, View):

    def get(self, request, subject_id):

        subjects = Subject.objects.all()

        return render(request, 'quiz/management/manager/created.html',{'subjects':subjects})



    def post(self, request, subject_id):

        if request.method == 'POST':

            title = request.POST.get('title')
            subjects = request.POST.get('subject')

            print(subjects)

            if Questionnaire.objects.filter(title = title).exists():
                messages.info(request, 'Ops.... Essa questão já foi adicionada no banco de dados ')
                return HttpResponseRedirect(reverse('quiz:quiz_detail', args  = [ subject_id ]))
            else:

                questions = Questionnaire(


                    id = uuid4(),
                    title = title
                    )
                questions.save()
                questions.subject.add(subjects)
                
                messages.success(request, 'Parabéns, A nova questão já foi adicionada no banco de dados')
                return HttpResponseRedirect(reverse('quiz:quiz_detail', args  = [ subject_id ]))