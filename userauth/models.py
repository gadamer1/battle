from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from mainapp.models import Problems

# Create your models here.



class Profile(models.Model):

    UNIV_CATEGORY=(
        ('korea','고려대'),
        ('yonsei','연세대'),
        ('others','그외')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img = models.ImageField(blank=True,null=True)
    problems_point = models.PositiveIntegerField(default=0)
    dungeon_point=models.PositiveIntegerField(default=0)
    univ = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=30,choices=UNIV_CATEGORY, default='others')
    problem_check = models.CharField(max_length=200,default='1',null=True)
    @classmethod
    def get_new(cls):
        return cls.objects.create().id


@receiver(post_save ,sender = User)
def update_user_profile(sender ,instance, created ,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)