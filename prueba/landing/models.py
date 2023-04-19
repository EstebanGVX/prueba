from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50)
    staff = models.BooleanField(default=False)

class Operations(models.Model):
    dateInit = models.DateField(auto_now=False,auto_now_add=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    boton1 = models.IntegerField(default=0)
    boton2 = models.IntegerField(default=0)
    timeInit = models.DateTimeField(auto_now=False, auto_now_add=False)
    timeFinal = models.DateTimeField(auto_now=False, auto_now_add=False)
    idUser = models.ForeignKey(Users, on_delete=models.CASCADE)