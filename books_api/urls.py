# from books_api import views
from django.urls import path,include
from .views import BookDetailView,AuthorDetailView
from . import views


urlpatterns=[
    path("",views.home_view,name="home"),
    path('author/',AuthorDetailView.as_view(),name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookDetailView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

]




















  # path('books/',views.show_all),
    # path('books/<int:pk>/',views.show),
    # path('createbook/',views.create_book),
    # path('updatebook/',views.update_book),
    # path('deletebook/',views.delete_book),
    # path('author/',views.show_all),