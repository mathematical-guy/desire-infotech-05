from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse("<h1>This is a Home Page !!!!</h1>")



def profile_page(request):
    value = render(request, 'profile656789876r-page.html')
    print("-----------------------------")
    print(value)
    print("-----------------------------")
    return value

def kuch_hi_naam_dedo(request):
    value = render(request, 'login.html')
    return value



def movie_list(request):

    movies = [{
        "name": "Hera Pheri",
        "year": 1999,
        "director": "Priya Darshan",
    }, 
    {

        "Name": "Avengers",
        "year": 2015,
        "director": "Marvel",
    },
    {

        "name": "Avengers",
        "Release Year": 2015,
        "director": "Marvel",
    }
    
    ]

    return render(request, "movies.html", context={"movies": movies})


def good_morning(request):
    return render(request, "good_morning.html", context={'ghjhg': 'Mohit'})

def game_list(request):
    game_names = [
        "Cricket",
        "PUBG",
        "FootBall",
        "Soccer",
        "WWE",
        "VolleyBall",
        "Kho-Kho",
        "Kabaddi",
        "Temple Run",
        "Angry Birds 2",
        "Valorant",
        "CS GO",
        "Prince of Persia",
        "Assasian Creeds",
        "Getting Over It",
    ]
    return render(request, "games.html", context={"game_names": game_names})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/', home_page),
    path('profile-page/', profile_page),
    path('login/', kuch_hi_naam_dedo),
    path('movies/', movie_list),
    path('good_morning/', good_morning),
    path('game_list/', game_list),
]
