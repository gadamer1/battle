from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Reply(models.Model):
    reply = models.OneToOneField(User,on_delete=models.CASCADE)
    contents= models.CharField(max_length=200, default='')
    created_date = models.TimeField(auto_now_add=True)

class Problems(models.Model):
    name = models.CharField(max_length=100,null=False)
    points = models.PositiveIntegerField(default=1)
    image=models.ImageField()
    check=models.PositiveIntegerField(default=0)
    answer = models.CharField(max_length=200,null=False,default='.')
    slug = models.SlugField(default='default')

class Dungeon(models.Model):
    check=models.PositiveIntegerField(default=0)



class Allpoints(models.Model):
    datetime = models.DateField(auto_now_add=True)
    korea_points = models.PositiveIntegerField(default=0)
    yonsei_points = models.PositiveIntegerField(default=0)
    others_points = models.PositiveIntegerField(default=0)
    
