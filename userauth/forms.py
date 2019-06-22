from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class MyPage(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('profile_img',)


class SignUpForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
        model = User
        fields= ['username','password1','password2','email']
        labels = {
            'username':'아이디',
            'password1':'비밀번호',
            'password2':'비밀번호 재확인',
            'email':'이메일'
        }