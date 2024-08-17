from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def track_list(request):
    track=[]
    track1={'id':1,'name':'python'}
    track2={'id':2,'name':'2D graphics'}
    track.append(track1)
    track.append(track2)
    context={}
    context['tracks']=track
    return render(request,'track/list.html',context)

def track_update(request, id):
    return  HttpResponse(f'<h1>update track number {id}</h1>')

def track_delete(reqest, id):
    return  HttpResponse(f'<h1>delete track number {id}</h1>')

def track_details(request, id):
    return  HttpResponse(f'<h1>details of track number {id}</h1>')

def track_create(request):
    return  HttpResponse(f'<h1>Account details</h1>')


