from django.shortcuts import render
from django.http import JsonResponse

from .models import Book

from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, TemplateView


# class BookView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         return render(request, 'book_list.html', context={'books': books})

#     def post(self,request):
#         data = request.POST

#         form = MyForm(data)
#         if form.is_valid():
#             form.save()
#             # Email bhejne ka logic idhar aayega
#             emails = ["abc@abc.com", "xyz@xyz.com", "abaaba@abaaba.com"]
#             for email in emails:
#                 try:
#                     send_email(emai)
#                 except Exception as e:
#                     print("EMail galat hai", email)
            
            
#             return render(request, 'book_list.html', context={'books': books})
        
#         else:
#             return render(request, 'book_list.html', context={'books': books})



# class LibraryView(View):
#     def get(self, request):
#         books = Library.objects.all()
#         return render(request, 'book_list.html', context={'books': books})

#     def post(self,request):
#         data = request.POST

#         form = MyForm(data)
#         if form.is_valid():
#             form.save()
#             # Email bhejne ka logic idhar aayega
#             emails = ["abc@abc.com", "xyz@xyz.com", "abaaba@abaaba.com"]
#             for email in emails:
#                 try:
#                     send_email(emai)
#                 except Exception as e:
#                     print("EMail galat hai", email)
            
            
#             return render(request, 'book_list.html', context={'books': books})
        
#         else:
#             return render(request, 'book_list.html', context={'books': books})



# class CoffeeShopView(View):
#     def get(self, request):
#         books = Coffee.objects.all()
#         return render(request, 'book_list.html', context={'books': books})




def book_list(request):
    # if request.method == "POST":
    #     data = request.POST

    #     form = MyForm(data)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'book_list.html', context={'books': books})
        
    #     else:
    #         return render(request, 'book_list.html', context={'books': books})

    # else:
    #     books = Book.objects.all()
    #     return render(request, 'book_list.html', context={'books': books})
    books = Book.objects.all()
    return render(request, 'book_list.html', context={'books': books})




class GeneralListView(View):
    model = None
    template_name = ""

    def get(self, request):
        objects = self.model.objects.all()

        return render(request, self.template_name, context={"objects": objects})
    

def myjson_view(request):
    return JsonResponse(data={
    'first_name': 'ABC',
    'last_name': 'XYZ',
    'movies': [
        'Movie1',
        'Movie2',
        'Movie3'
    ]
})

# class BookView(GeneralListView):
#     model = Book
#     template_name = "book-list.html"

# class CoffeeView(GeneralListView):
#     model = Coffee
#     template_name = "coffee-list.html"


class MyBookListView(ListView):
    model = Book
    template_name = "book_list2.html"
    context_object_name = "books"

class WelcomePage(TemplateView):
    template_name = 'welcome.html'