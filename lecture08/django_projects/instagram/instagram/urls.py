"""instagram URL Configuration

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
from django.http import HttpResponse
from django.shortcuts import render


def home_page(qwedfghjk):
    content = """
        <h1 style="color: green;">Hello Home Page</h1>
        <h3 style="color: red;">Hello Home Page</h3>
    """
    return HttpResponse(content=content)


def new_page(request):
    value = render(request=request, template_name="myfile.html")
    print(value)
    return value



urlpatterns = [
    path('admin/', admin.site.urls),
    path('kivant/', home_page),
    path('new-page/', new_page),
]
