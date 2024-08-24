from django.db import models
from track.models import *
from django.urls import reverse
from django.shortcuts import redirect

# Create your models here.

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    image=models.ImageField(upload_to='trainee/images/',blank=True,null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    trackobj=models.ForeignKey("track.Track",on_delete=models.CASCADE )

    def getimage(self):
        return f'/media/{self.image}'

    def get_list_url():
        return reverse('trainee_list')

    @classmethod
    def create(cls,name,image,email,age,address,trackid):
        traineeobj = Trainee() 
        traineeobj.name= name
        traineeobj.image= image
        traineeobj.email= email
        traineeobj.age= age
        traineeobj.address= address
        traineeobj.trackobj=Track.objects.get(pk=trackid)
        traineeobj.save()
        return redirect(cls.get_list_url())
   
   