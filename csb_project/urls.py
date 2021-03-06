"""csb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.sign_in, name='signin'),
    path('signup', views.sign_up, name='signup'),
    path('user/', views.user_view, name='user_view'),
    path('send_message/', views.send_message, name='send_message'),
    path('update_password/', views.update_password, name='update_password'),
    path('find_messages/', views.find_messages, name='find_messages'),
    #for development path('delete_db/', views.delete_db, name='delete_db'),
]
