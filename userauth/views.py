from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else :
                return redirect('mainapp:main')
    else:
        form = AuthenticationForm()
    return render(request,'userauth/login/login.html',{'form':form})

def signup(request):
    return render(request,'userauth/sign_up/sign_up.html')

def korea(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if '@korea.ac.kr' in form.cleaned_data.get('email'):
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal              
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('userauth:dummy_korea')
    else:
        form = SignUpForm()
    return render(request,'userauth/sign_up/korea.html',{'form':form})


def yonsei(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('email') in 'yonsei@ac.kr':
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.univ = 'yonsei'       
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('userauth:mypage')
    else:
        form = SignUpForm()
    return render(request,'userauth/sign_up/yonsei.html',{'form':form})

def others(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.univ = ''         
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('userauth:mypage')
    else :
        form = SignUpForm()
    return render(request,'userauth/sign_up/others.html',{'form':form})

@login_required(login_url ='login/login/')
def mypage(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'userauth/mypage/mypage.html',{'profile':profile})

@login_required(login_url ='login/login/')
def logout_view(request):
    logout(request)
    return redirect('mainapp:main')

@login_required(login_url ='login/login/')
def dummy_korea(request):
    request.user.profile.univ = 'korea'
    request.user.profile.category='korea'
    request.user.profile.save()
    print(request.user.profile.univ)
    return redirect('userauth:mypage')


@login_required(login_url ='login/login/')
def dummy_yonsei(request):
    request.user.profile.univ = 'yonsei'
    request.user.profile.category='yonsei'
    request.user.profile.save()
    return redirect('userauth:mypage')