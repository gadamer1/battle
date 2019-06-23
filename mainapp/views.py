from django.shortcuts import render,redirect
from .models import Problems,Reply
from userauth.models import Profile
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProblemForm,ReplyForm
# Create your views here.


def main(request):
    comments = Reply.objects.all().order_by('created_date').reverse()
    page = request.GET.get('page','1')
    page = int(page)
    num=10
    paginator = Paginator(comments,num)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5   
    page_range = range(start_index,end_index+1)





    koreapoints = 0
    yonseipoints =0
    korea = Profile.objects.filter(category='korea')
    for instance in korea:
        koreapoints+=instance.problems_point + instance.dungeon_point
    yonsei = Profile.objects.filter(category='yonsei')
    
    for instance in yonsei:
        yonseipoints+=instance.problems_point + instance.dungeon_point

    if request.method =='POST':
        form = ProblemForm(request.POST)
        reply_form = ReplyForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='V1hwT1YyRnNhM2xXYm5CcVpIb3dPUT09':
                if 'cooooooorrrrrreeeeccctt' not in request.user.profile.problem_check:
                    request.user.profile.problem_check+='cooooooorrrrrreeeeccctt'
                    request.user.profile.dungeon_point+=200
                    request.user.profile.save()
                    return redirect('userauth:myuser')
                else:
                    return render(request,'mainapp/main/main.html',{'form':form,'alert':True,'koreapoint':koreapoints
    ,'yonseipoint':yonseipoints})
            else:
                return render(request,'mainapp/main/main.html',{'form':form,'flag':True,'koreapoint':koreapoints
    ,'yonseipoint':yonseipoints})
        if reply_form.is_valid():
            try:
                instance = Reply.objects.get(author=request.user)
                messages.warning(request,'응원은 한번만 하실 수 있습니다.')
            except Reply.DoesNotExist:
                instance = reply_form.save(commit=False)
                instance.author = request.user
                instance.publish()
    else:
        form = ProblemForm()
        reply_form = ReplyForm()
    
    return render(request,'mainapp/main/main.html',{'form':form,'reply_form':reply_form,'koreapoint':koreapoints
    ,'yonseipoint':yonseipoints,'comments':p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})


@login_required(login_url ='../login/login/')
def problems_list(request):
    problems = Problems.objects.all().order_by('id')
    page = request.GET.get('page','1')
    page = int(page)
    num=5
    paginator = Paginator(problems,num)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5   
    page_range = range(start_index,end_index+1)
    return render(request,'mainapp/problems/problems_list.html',{'problems':p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})


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


def reply_delete(request, author_id):
    return redirect('')

def reply_update(request,author_id):
    return redirect('')