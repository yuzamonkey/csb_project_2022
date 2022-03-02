from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Message
from .utils import user_is_in_db
from django.db import connection

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM csb_project_message")
# messages = cursor.fetchall()


def index(request):
    return render(request, 'index.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user_is_in_db(username):
            user = User.objects.filter(username=username)[0]
            if user.password == password:
                return redirect(f"../user/?username={username}&password={password}")
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


def user_view(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    if not user_is_in_db(username):
        return HttpResponse('Invalid username')
    user = User.objects.filter(username=username)[0]
    if user.password != password:
        return HttpResponse('Invalid password')

    messages = Message.objects.filter(receiver=user)
    users = User.objects.exclude(username=username)
    params = {
        'username': username,
        'messages': messages,
        'users': users
    }
    return render(request, 'user.html', params)


def send_message(request):
    sender = User.objects.filter(username=request.POST.get('sender'))[0]
    receiver = User.objects.filter(username=request.POST.get('receiver'))[0]
    content = request.POST.get('content')
    new_message = Message(sender=sender, receiver=receiver, content=content)
    new_message.save()
    return redirect(f"../user/?username={sender.username}&password={sender.password}")


def update_password(request):
    user = User.objects.filter(username=request.POST.get('username'))[0]
    new_password = request.POST.get('password')
    user.password = new_password
    user.save()
    return redirect(f"../user/?username={user.username}&password={new_password}")


def delete_db(request):
    Message.objects.all().delete()
    User.objects.all().delete()
    return redirect(index)
