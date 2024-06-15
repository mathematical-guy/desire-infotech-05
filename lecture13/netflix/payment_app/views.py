from django.shortcuts import render
from payment_app.models import Card, User
from django import forms
from django.views.decorators.csrf import csrf_exempt


class AddCardForm(forms.ModelForm):
    class Meta:
        model = Card
        # fields = ("cvv", "owner_name")
        fields = "__all__"


def myfile_view(request):
    form = AddCardForm()
    return render(request, "myfile.html", context={"myform": form,})



class NewUserForm(forms.ModelForm):
    # birth_date = forms.DateField(widget={"type": forms.DateInput()})
    age = forms.IntegerField(min_value=18)

    class Meta:
        model = User
        fields = ("name", "is_indian", "skills", "age")

@csrf_exempt
def new_user(request):
    # print(request.method)
    if request.method == "POST":
        myform = NewUserForm(request.POST)
        print("Form is Valid or Not?", myform.is_valid())
        print(myform.errors)
        return render(request, "user-form.html", context={"new_form": myform})
    print("POST: ", request.POST)
    myform = NewUserForm()
    return render(request, "user-form.html", context={"new_form": myform})