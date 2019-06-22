from django.contrib import admin
from django.urls import path
from . import views

app_name = 'userauth'

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup'),
    path('mypage/',views.mypage,name='mypage'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/korea/',views.korea,name= 'korea'),
    path('signup/yonsei/',views.yonsei,name= 'yonsei'),
    path('signup/others/',views.others, name= 'others'),


    path('dummy/korea/',views.dummy_korea,name='dummy_korea'),
    path('dummy/yonsei/',views.dummy_yonsei,name='dummy_yonsei'),
]
