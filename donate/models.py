from django.db import models

# Create your models here.

class Facebook(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


    def __str__(self): 
        return self.username

class Instagram(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


    def __str__(self): 
        return self.username


class Google(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


    def __str__(self): 
        return self.username
    