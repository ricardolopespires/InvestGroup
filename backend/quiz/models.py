from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from .fields import OrderField
from django.db import models
from uuid import uuid4
# Create your models here.





class Quiz(models.Model):

    id = models.CharField(max_length = 150, primary_key = True, unique = True)
    order = models.IntegerField(help_text = 'O numero da questao', default = 1)    
    name = models.CharField(max_length=100)   
    slug = models.SlugField(blank=True)
    description = models.TextField(help_text = 'Descrição do Assuntos do questionario')
    created = models.DateTimeField( auto_now_add = False)
    topic = models.CharField(max_length = 150, blank = True, help_text = 'O tópico do questionário')
    questions = models.ManyToManyField("quiz.Question", related_name="question_list")
    percentage = models.IntegerField( help_text = 'A porcentagem do usuários', default = 0)
    total = models.IntegerField(help_text = 'O total de questionarios', default = 0)
    active = models.BooleanField(default=False)
    timestamp = models.IntegerField(help_text = 'Duração do questionarios')

    class Meta:
        ordering = ['timestamp',]
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return f'{self.name}'


    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):    

    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    name = models.CharField(max_length = 400)
    answers = models.ManyToManyField("quiz.Answer", related_name="questions_answer", blank=True) 
    createdAt =  models.DateTimeField(auto_now_add = True)
    updatedAt =  models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name


        def get_answers(self):
            return self.answer_set.all()


class Answer(models.Model):
   
  
    question = models.ForeignKey(Question,  on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)   
    score = models.IntegerField( default = 0)    
    
    def __str__(self):
        return f"{self.name}"


class QuizTaker(models.Model):

    
    id = models.CharField(max_length = 190, primary_key = True, unique = True)   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField( default = 0)
    completed = models.BooleanField( default = False)
    date_finished = models.DateTimeField( null = True)
    timestamp = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return f'{self.quiz}'


class UsersAnswer(models.Model):

    id = models.CharField(max_length = 190, primary_key = True, unique = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) 
    question = models.ForeignKey(Question, on_delete = models.CASCADE,null = True)
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE, null = True)
    score = models.IntegerField( default = 0,null = True)
    completed = models.BooleanField( default = False,null = True)
    date_finished = models.DateTimeField( null = True)

    def __str__(self):
        return self.question.label


@receiver(pre_save, sender = Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)




