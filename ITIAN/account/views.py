from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def account_list(request):
   return  HttpResponse('<h1>Account list</h1>')

def account_update(request):
    return  HttpResponse(f'<h1>Update account</h1>')

def account_create(request):
    return  HttpResponse(f'<h1>Create account</h1>')

def account_delete(request):
    return  HttpResponse(f'<h1>Delete account</h1>')

def account_details(request):
    return  HttpResponse(f'<h1>Account details</h1>')
