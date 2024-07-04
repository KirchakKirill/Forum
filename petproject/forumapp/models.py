from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(null=False, blank=False, max_length=255)
    password = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(null=False, blank=False,   max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'forumapp'
        verbose_name = 'users'


