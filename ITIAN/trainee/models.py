from django.db import models
from track.models import *

# Create your models here.

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    image=models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    trackobj=models.ForeignKey("track.Track",on_delete=models.CASCADE )