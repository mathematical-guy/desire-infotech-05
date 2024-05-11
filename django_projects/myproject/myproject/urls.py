"""myproject URL Configuration

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
import random


def mypage(x):
    data = """
        <!DOCTYPE html>
        <html lang="en">
        <body>
            <h1>Hello World</h1>
            <h2>Hello World H2</h2>
            <h6>Hello World H6</h6>
            h3
        </body>
        </html>
        """
    return HttpResponse(data)

def mypagenew(x):
    number = random.randint(1, 10000)
    print(x, type(x))
    
    return HttpResponse("<h1>" + str(number) + "</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myurl/', mypage),
    path('my-new-url/', mypagenew),
]
