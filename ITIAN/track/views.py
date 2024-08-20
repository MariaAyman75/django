from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def track_list(request):
    context={}
    tracks=Track.objects.all()
    context['tracks']=tracks
    return render(request,'track/list.html',context) 

def track_update(request, id):
    return  HttpResponse(f'<h1>update track number {id}</h1>')

def track_delete(reqest, id):
    return  HttpResponse(f'<h1>delete track number {id}</h1>')

def track_details(request, id):
    context={'track':Track.objects.get(pk=id)}
    return render(request,'track/details.html',context)


def track_create(request):
    context={}
    if(request.method=='POST'):
        context={}
        if(len(request.POST['trackname'])>0 and len(request.POST['trackname'])<=50):
            trackobj=Track()
            trackobj.name=request.POST['trackname']
            trackobj.save()
            # return redirect('track:track_list')
        else:
            context['error']='invalid'
    return render(request,'track/create.html',context)
    # return  HttpResponse(f'<h1>Account details</h1>')


