from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

def index(request):
    #return render(request, 'pages/index.html')
    return HttpResponse('Welcome')

def sign_in(request):
    #return render(request, 'pages/index.html')
    return HttpResponse('Sign in')

def sign_up(request):
    #return render(request, 'pages/index.html')
    return HttpResponse('Sign up')