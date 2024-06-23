from django.shortcuts import render, redirect
from new_app.models import Device
from django.contrib.auth.decorators import login_required
from django import views
from django.views.generic import ListView


def device_list(request):
    # if not request.user.is_authenticated:
    #     return redirect('admin:login')
    
    devices = Device.objects.all()
    if request.method == "POST":
        "post logic"
    else:
        "get logic"

    return render(request, 'devices-list.html', context={"devicess": devices})


def device_detail(request, deffdfd):
    try:
        device = Device.objects.get(id=deffdfd)
        return render(request, 'devices-detail.html', context={"device": device})
    except Exception as e:
        print(e)
        # return redirect
        return render(request, 'devices-detail.html')




class DeviceView(views.View):
    # def post(self, request):
    #     print(request.POST)
    #     return render(request, 'devices-list.html')

    def get(self, request):
        devices = Device.objects.all()
        return render(request, 'devices-list.html', context={"devicess": devices})
class UserView(views.View):
    def get(self, request):
        from django.contrib.auth.models import User

        users = User.objects.all()
        return render(request, 'user-list.html', context={"users": users})
    
class IndianView(views.View):
    def get(self, request):
        from myapp.models import Indian

        indians = Indian.objects.all()
        return render(request, 'indians-list.html', context={"indians": indians})
    


class DeviceListView(ListView):
    model = Device
    template_name = 'devices-list.html'
    context_object_name = 'devicess'