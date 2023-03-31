from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=100)
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

class signup(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=200)
    passw = models.CharField(max_length=20)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def __str__(self):
        return str(self.user)

STATUS_CHOICES = (
        ('send', 'send'),
        ('accepted', 'accepted')
    )

class Relationship(models.Model):
    sender = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

