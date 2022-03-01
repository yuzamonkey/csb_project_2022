from django.db import models

class User(models.Model):
    username = models.TextField()
    password = models.TextField()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)