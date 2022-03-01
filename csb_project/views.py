from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

def index(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'signin.html')

def sign_up(request):
    return render(request, 'signup.html')