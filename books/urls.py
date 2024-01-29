from django.urls import path
from .views import BookListView, BookDetailView


app_name = 'books'
urlpatterns = [
  path('', BookListView.as_view(), name='book-list'),
  path('<int:pk>/book-detail/', BookDetailView.as_view(), name='book-detail'),
  # path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]