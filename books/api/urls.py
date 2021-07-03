from django.urls import path

from books.api import views

urlpatterns = [
    path('books/', views.books, name="books_list"),
    path('db/', views.books, name="database_update"),
]