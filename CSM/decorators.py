from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("CSM:home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("CSM:loginPage")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group  = None
            if request.user.group.existe():
                group = request.user.group.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are Not Authorized to view this page !')
                 
        return wrapper_func
    return decorators