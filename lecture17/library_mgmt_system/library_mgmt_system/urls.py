from django.contrib import admin
from django.urls import path
from book_app.views import book_list, MyBookListView, WelcomePage, myjson_view
from member_mgmt.views import BookDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list),
    path('mybooks/', MyBookListView.as_view()),
    path('welcome_page/', WelcomePage.as_view()),
    path('myjson_view/', myjson_view),
    path('book_detail/<int:id>/', BookDetail.as_view()),
]
