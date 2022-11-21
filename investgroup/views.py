from quiz.models import Quiz, Question, QuizTaker, UsersAnswer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.views.generic import View
from django.shortcuts import render
from datetime import date
from uuid import uuid4









class Index_View(View):

    def get(self, request):
        return render(request,'initial/index.html')





@api_view(['POST'])
@csrf_exempt
def save_question_result(request):
    data = request.data

    question = data.get('question_uid')
    answer = data.get('answer_uid')

    print(question)

    if question_uid is None and answer_uid is None:
        payload = {'data' : 'both question uid and answer uid are required' , 'status' : False}

        return Response(payload)

    codigo_id = str(uuid4())

    result = UsersAnswer.objects.get_or_create(

        id = codigo_id,
        question = question,
        answer = answer,
        score = 0,
        completed = True,
        date_finished = data.today()
        )

    result.save()

    #payload = {'data' : question_obj.calculate_percentage() , 'status' : True}

    return Response(result)

