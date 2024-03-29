from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('main/',views.main, name='main'),
    path('',views.main),
    path('ranking/',views.ranking, name='ranking'),
    path('problems/',views.problems_list,name='problems_list'),
    path('problems/<slug:problems_slug>/',views.problems, name='problems'),
    path('reply/delete/<slug:id>/',views.reply_delete,name='reply_delete'),
    path('reply/update/<slug:id>/',views.reply_update,name='reply_update'),
]
