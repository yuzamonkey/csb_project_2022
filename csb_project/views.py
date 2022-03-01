from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Message

def index(request):
    users = User.objects.all()
    print ("Users", users, len(users))
    for u in users:
        print("U", u.username)
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'signin.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print("POST METHOD CALLED", username)
        # if username is taken
        new_user = User(username=username, password='password')
        new_user.save()
        return HttpResponse('ok')
    return render(request, 'signup.html')
