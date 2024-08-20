from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from track.models import *


# Create your views here.

def trainee_list(request):
    context={}
    trainees=Trainee.objects.all()
    context['trainees']=trainees
    return render(request,'trainee/list.html',context)

def trainee_update(request, id):
    context = {}
    context = {"id": id}
    return render(request, "trainee/update.html", context)

def trainee_delete(request, id):
    context = {}
    context = {"id": id}
    return render(request, "trainee/delete.html", context)

def trainee_details(request, id):
    context={'trainee':Trainee.objects.get(pk=id)}
    return render(request,'trainee/details.html',context)

def trainee_create(request):
    context={}
    context['tracks']=Track.objects.all()
    if(request.method=='POST'):
        context={}
        if(len(request.POST['traineename'])>0 and len(request.POST['traineename'])<=100):
            traineeobj=Trainee()
            traineeobj.name=request.POST['traineename']
            traineeobj.email=request.POST['traineeemail']
            traineeobj.age=request.POST['traineeage']
            traineeobj.address=request.POST['traineeaddress']
            traineeobj.trackobj=Track.objects.get(pk=request.POST['traineetrackid'])
            traineeobj.save()
            # return redirect('trainee:trainee_list')
        else:
            context['error']='invalid'
    return render(request,'trainee/create.html',context)
