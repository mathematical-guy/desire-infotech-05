from django.shortcuts import render

from new_app.forms import PhoneForm

def home_view(request):
    return render(request, 'home.html')

def about_view(request):

    if request.method == "GET":
        form = PhoneForm()
    else:
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            form = PhoneForm()
            
    return render(request, 'about.html', context={'form': form})

def delete_view(request):
    return render(request, 'delete.html')