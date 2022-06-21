from django.shortcuts import redirect
from django.http import HttpResponse

def redirect_authenticated_user(view_func):
    def wrapper_func(request,*args,**kwarg):
        if request.user.is_authenticated :
            return redirect('/index/')
        else :
            return view_func(request,*args,**kwarg)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def warpper_func(request,*args,**kwarg):
            group = None
            if request.user.groups.exists() :
                group = request.user.groups.all()[0].name
            if group in allowed_roles :
                return view_func(request,*args,**kwarg)
            else :
                return HttpResponse('你未被授權瀏覽此頁面!!')
        return warpper_func
    return decorator