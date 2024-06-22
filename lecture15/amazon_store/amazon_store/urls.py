"""amazon_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from new_app.views import home_view, about_view, delete_view


def file_view(request):
    value =  render(request, 'file.html')
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('login')
    # value.set_cookie('naya-key-hai', 'rtyujkluytrer', max_age=10)
    # value.set_signed_cookie(request.get_signed_cookie('key11', 'valuye1'))
    # print(value)
    return value


def mynewview(request):
    # print(request.COOKIES.get('sessionid'))
    is_login = request.COOKIES.get('is_login')
    if is_login == 'yes':
        return HttpResponse("<h1>Hello From new View </h1>")
    else:
        return HttpResponse("<h1>You are not logged in</h1>")
    

def login_view(request):
    context = {}
    value = render(request, 'login.html', context=context)
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return value
        else:
            login(request=request, user=user)
            # return render(request, 'file.html')
            # return redirect(file_view)        # View Name
            return redirect('naya-name')          # URL name

        # if username == 'sameer' and password == 'india':
        #     context = {"message": "Correct Credentials"}
        #     value.set_cookie('is_login', 'yes')
        # else:
        #     context = {"message": "InCorrect Credentials"}


    return value


urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/', file_view, name='naya-name'),
    path('mynewview/', mynewview),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('delete/', delete_view, name='delete'),
]
