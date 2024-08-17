from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def trainee_list(request):
    trainee=[]
    trainee1={'id':1,'name':'maria','email':'maria@gmail.com','age':23,'address':'El-Fayoum','trackID':1}
    trainee2={'id':2,'name':'marina','email':'marina@gmail.com','age':23,'address':'El-Fayoum','trackID':2}
    trainee.append(trainee1)
    trainee.append(trainee2)
    context={}
    context['trainees']=trainee
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
    context = {}
    context = {"id": id}
    return render(request, "trainee/details.html", context)

def trainee_create(request):
    return render(request, "trainee/create.html")
