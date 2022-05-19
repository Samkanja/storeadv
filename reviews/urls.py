from django.urls import path
from . import views

urlpatterns = [
    # path('',views.welcomeView,name='welcomeView')
    path('books/',views.bookList, name='book_list'),
    path('books/<int:pk>/',views.book_detail,name='book_detail'),

]