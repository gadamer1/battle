from django.shortcuts import render,redirect
from .models import Problems
from userauth.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProblemForm
# Create your views here.


def main(request):
    if request.method =='POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='V1hwT1YyRnNhM2xXYm5CcVpIb3dPUT09':
                if 'cooooooorrrrrreeeeccctt' not in request.user.profile.problem_check:
                    request.user.profile.problem_check+='cooooooorrrrrreeeeccctt'
                    request.user.profile.dungeon_point+=200
                    request.user.profile.save()
                    return redirect('userauth:myuser')
                else:
                    return render(request,'mainapp/main/main.html',{'form':form,'alert':True})
            else:
                return render(request,'mainapp/main/main.html',{'form':form,'flag':True})
    else:
        form = ProblemForm()
    return render(request,'mainapp/main/main.html',{'form':form})


@login_required(login_url ='login/login/')
def problems_list(request):
    problems = Problems.objects.all().order_by('id')
    return render(request,'mainapp/problems/problems_list.html',{'problems':problems})


def problems(request ,problems_slug):
    problem = Problems.objects.get(slug=problems_slug)
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']==problem.answer:
                print(request.user.profile.problem_check)
                if problem.name not in request.user.profile.problem_check:
                    request.user.profile.problem_check += problem.name
                    request.user.profile.problems_point+=problem.points
                    request.user.profile.save()
                    return redirect('mainapp:problems_list')
                else:
                    return render(request,'mainapp/problems/problems.html',{'form':form,'alert':True,'problems':problem})
            else:
                return render(request,'mainapp/problems/problems.html',{'form':form,'flag':True,'problems':problem})
    else:
        form = ProblemForm()
    return render(request,'mainapp/problems/problems.html',{'form':form,'problems':problem})


def ranking(request):
    p_koreapoints=0
    d_koreapoints=0
    p_yonseipoints=0
    d_yonseipoints=0
    koreapoints=0
    yonseipoints=0
    profiles_korea = Profile.objects.filter(category='korea')

    for profile_korea in profiles_korea:
        p_koreapoints+=profile_korea.problems_point
        d_koreapoints+=profile_korea.dungeon_point
    koreapoints=p_koreapoints+d_koreapoints
    yonseipoints=p_yonseipoints+d_yonseipoints
    profiles_yonsei = Profile.objects.filter(category='yonsei')
    for profile_yonsei in profiles_yonsei:
        p_yonseipoints+=profiles_yonsei.problems_point
        d_yonseipoints+=profiles_yonsei.dungeon_point

    p_korea_ranker = Profile.objects.filter(category='korea').order_by('problems_point').reverse()
    p_korea_ranker = p_korea_ranker[:10]

    d_korea_ranker = Profile.objects.filter(category='korea').order_by('dungeon_point').reverse()
    d_korea_ranker = d_korea_ranker[:10]

    p_yonsei_ranker = Profile.objects.filter(category='yonsei').order_by('problems_point').reverse()
    p_yonsei_ranker = p_yonsei_ranker[:10]
    d_yonsei_ranker = Profile.objects.filter(category='yonsei').order_by('dungeon_point').reverse()
    d_yonsei_ranker = d_yonsei_ranker[:10]
    return render(request , 'mainapp/ranking/ranking.html',{'p_yonseipoints':p_yonseipoints,
    'd_yonseipoints':d_yonseipoints,'p_koreapoints':p_koreapoints,'d_koreapoints': d_koreapoints,
    'koreapoints':koreapoints,'yonseipoints':yonseipoints,'p_korea_ranker':p_korea_ranker,
    'd_korea_ranker':d_korea_ranker,'d_yonsei_ranker':d_yonsei_ranker,'p_yonsei_ranker':p_yonsei_ranker
    })
