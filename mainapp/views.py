from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

from .decorators import *
from .filters import *
from .models import *
from .forms import *

@redirect_authenticated_user
def register(request):
    form = RegisterForm()
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username','')
            messages.success(request,'帳號建立成功' + ' ' + username)
            return redirect('/login/')
    return render(request,'accounts/register.html',locals())

@redirect_authenticated_user
def login(request):
    if request.method == 'POST' :
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            if user.is_active :
                auth.login(request,user)
                return redirect('/index/')
            else :
                messages.error(request,'帳號尚未生效')
        else :
            messages.error(request,'登入失敗')

    return render(request,'accounts/login.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/')

@redirect_authenticated_user
def guest(request):
    news = News.objects.all().order_by('-date_created')
    myfilter = NewsFilter(request.GET,queryset=news)
    news = myfilter.qs
    filtervalue = request.GET.get('title','')
    categories = Category.objects.all()
    
    paginator = Paginator(news,8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request,'news/guest.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index(request):
    news = News.objects.all().order_by('-date_created')
    myfilter = NewsFilter(request.GET,queryset=news)
    news = myfilter.qs
    filtervalue = request.GET.get('title','')
    categories = Category.objects.all()

    paginator = Paginator(news,8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request,'news/index.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin'])
def createnew(request):
    form = CreateNewForm()
    if request.method == 'POST' :
        form = CreateNewForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('/index/')
    else:
        form = CreateNewForm()
    return render(request,'news/createnew.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin'])
def updatenew(request,pk=None):
    new = News.objects.get(id=pk)
    form = UpdateForm(instance=new)
    if request.method == 'POST' :
        form = UpdateForm(request.POST,request.FILES,instance=new)
        if form.is_valid() :
            form.save()
            return redirect('/index/')
    else :
        form = UpdateForm(instance=new)
    return render(request,'news/updatenew.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin'])
def deletenew(request,pk=None):
    new = News.objects.get(id=pk)
    new.delete()
    
    return redirect('/index/')

def detail(request,pk=None):
    new = News.objects.get(id=pk)
    new.press += 1
    new.save()
    if request.method == 'POST' :
        PostComment.objects.create(
            author = request.user.profile,
            post = new,
            content = request.POST.get('content','')
        )
        messages.success(request,'建立留言成功!!')
        return redirect('/detail/' + str(new.id) + '/')
    return render(request,'news/detail.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def accountsetting(request):
    profile = request.user.profile
    form = AccountsettingForm(instance=profile)
    if request.method == 'POST' :
        userform = UserForm(request.POST,instance=request.user)
        if userform.is_valid() :
            userform.save()
            
        form = AccountsettingForm(request.POST,request.FILES,instance=profile)
        if form.is_valid() :
            form.save()
            return redirect('/index/')
    return render(request,'accounts/accountsetting.html',locals())
