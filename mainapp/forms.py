from django import forms
from . import models
from .models import Reply
class ProblemForm(forms.Form):
    answer= forms.CharField(label='',max_length=100,required=True)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['contents']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contents'].label = "댓글"