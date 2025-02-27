from django.urls import path
from . import views

urlpatterns = [
    # URLs de Author
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/new/', views.author_create, name='author_create'),
    path('authors/<int:pk>/edit/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),

    # URLs de Book
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    #Url por defecto
    path('', views.home, name='home'), 

]
