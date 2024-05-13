import random
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


def new_view(request):
    return HttpResponse(content="<h1>Hello Mohit, How are you ?</h1>")



def home_page(request):
    # names = ["Aarav", "Aarush", "Aayush", "Avyaan", "Advik", "Akarsh", "Anay", "Atharva", "Arhaan", "Ahaan", "Arnav", "Adhrit",]
    # name = random.choice(names)
    # name = "Mohit"
    return render(request, 'home.html')



def profile_page(request):
    return render(request, 'abdefgh.html')



def login_page(request):
    return render(request, 'login.html')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('url-ka-name/', new_view),
    path('home_page/', home_page),
    path('login/', login_page),
    path('profile/', profile_page),
]
