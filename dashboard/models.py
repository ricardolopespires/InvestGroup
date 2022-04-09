from django.db import models

# Create your models here.


class Setor(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name



class Acoes(models.Model):
    setor = models.ForeignKey(Setor, related_name = 'setor_acoes', on_delete = models.CASCADE)
    id = models.CharField(primary_key = True, max_length =150)
    name = models.CharField(max_length = 150 )
    images = models.ImageField(max_length = 150, )
    


    def __str__(self):
        return self.name






