from django.db import models

# Create your models here.





class Subject(models.Model):
    id = models.CharField(max_length = 190, primary_key = True, unique = True)
    title = models.CharField(max_length = 150, help_text = 'Titulo do assunto do questionario')
    description = models.TextField(help_text = 'Descrição do Assuntos do questionario')
    created = models.DateTimeField( auto_now_add = False)
    percentage = models.IntegerField( help_text = 'A porcentagem do usuários', default = 0)
    total = models.IntegerField(help_text = 'O total de questionarios', default = 0)
    questionnaire = models.ManyToManyField('quiz.Questionnaire', related_name = 'subject_questionnaire', blank = True)
    usuario = models.ManyToManyField( 'accounts.User', related_name = 'subject_usuario', blank = True)

        

    def __str__(self):
        return  f'{self.title}'


    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'




class Questionnaire(models.Model):

    id = models.CharField(max_length = 190, primary_key = True, unique = True)
    title = models.CharField(max_length = 400, help_text = 'A Perguntas do questionario')
    subject = models.ManyToManyField('quiz.Subject', related_name = 'questionario_assunto')
        

    def __str__(self):
        return  f'{self.title}'


    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'



class Questions(models.Model):

    id = models.CharField(max_length = 190, primary_key = True, unique = True)    
    questionnaire = models.ForeignKey(Questionnaire, related_name = 'questionario', on_delete = models.CASCADE)
    answers = models.CharField(max_length = 400, help_text = 'respostas')
    correct = models.BooleanField()
    valor = models.IntegerField()
    usuario = models.ManyToManyField('accounts.User', related_name = 'questoes', blank = True)


    def __str__(self):
        return  f'{self.answers}'

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'



class Perfil(models.Model):

    STATUS_CHOICES = (

        ('cconservador','Conservador'),
        ('moderado','Moderado'),
        ('dinâmico','Dinâmico'),
        ('arrojado','Arrojado'),
        ('Agressivo','Agressivo'),
        )

    id = models.CharField(max_length = 190, primary_key = True, unique = True)
    investor = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador')
    description = models.TextField()
    risk_profile = models.CharField(max_length = 150,)
    minimum = models.IntegerField()
    maximum = models.IntegerField()


    def __str__(self):
        return f'{self.investor}'
