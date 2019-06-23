from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display=['get_name']
    def get_name(self,obj):
        return obj.user.username

admin.site.register(Profile,ProfileAdmin)