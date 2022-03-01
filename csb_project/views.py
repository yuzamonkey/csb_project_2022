from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Message
from .utils import user_is_in_db

def index(request):
    users = User.objects.all()
    print ("Users", users, len(users))
    for u in users:
        print("U", u.username)
    return render(request, 'index.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user_is_in_db(username):
            user = User.objects.filter(username=username)[0]
            if user.password == password:
                return HttpResponse('Authentication done')
            else:
                return render(request, 'signin.html', {'message': 'Wrong credentials'})
        else:
            return render(request, 'signin.html', {'message': 'Wrong credentials'})
    return render(request, 'signin.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if user_is_in_db(username): 
            return render(request, 'signup.html', {'message': f'Username "{username}" is taken'})
        new_user = User(username=username, password='password')
        new_user.save()
        return redirect(sign_in)
    return render(request, 'signup.html')
