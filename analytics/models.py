from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.







class Selic(models.Model):  
    data = models.DateTimeField(auto_now = False, null=True, blank=True )
    taxa = models.CharField(max_length = 10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True,null=True, blank=True)
