from django.shortcuts import render

from myapp.models import Movie

def add_movie_view(request):
    print(request.POST)

    if request.method == "POST":
        name = request.POST.get("name")
        type = request.POST.get("type")
        release_date = request.POST.get("release_date")

        Movie.objects.create(name=name, release_date=release_date, type=type)
    return render(request, "add-movie.html")


def movie_list(request):
    print(request.GET)
    name = request.GET.get('name')
    movies = Movie.objects.all().order_by('?')
    if name:
        movies = movies.filter(name__icontains=name)
    return render(request, "movie-list.html", context={"movies": movies})

