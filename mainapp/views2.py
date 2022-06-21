from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from .filters import *
from .decorators import *
from .models import *
from .forms import *

@redirect_authenticated_user
def guest_category1(request):
    catego = '焦點'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/guest_category.html',locals())

@redirect_authenticated_user
def guest_category2(request):
    catego = '國際'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/guest_category.html',locals())

@redirect_authenticated_user
def guest_category3(request):
    catego = '政治'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/guest_category.html',locals())

@redirect_authenticated_user
def guest_category4(request):
    catego = '娛樂'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/guest_category.html',locals())

@redirect_authenticated_user
def guest_category5(request):
    catego = '運動'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/guest_category.html',locals())

@redirect_authenticated_user
def guest_category6(request):
    catego = '生活'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/guest_category.html',locals())

@redirect_authenticated_user
def guest_category7(request):
    catego = '健康'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/guest_category.html',locals())   


@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index_category1(request):
    catego = '焦點'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/index_category.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index_category2(request):
    catego = '國際'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/index_category.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index_category3(request):
    catego = '政治'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/index_category.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index_category4(request):
    catego = '娛樂'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/index_category.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index_category5(request):
    catego = '運動'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/index_category.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index_category6(request):
    catego = '生活'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/index_category.html',locals())

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin','customer'])
def index_category7(request):
    catego = '健康'
    news = News.objects.filter(category__name=catego).order_by('-date_created')
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
    return render(request,'category/index_category.html',locals())


