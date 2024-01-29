from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views import View
from books.models import Books

# Create your views here.
class BookListView(View):
  def get(self, request):
    books = Books.objects.order_by('create_at')
    context = {
      'books' : books
    }
    return render(request, template_name='book/book_list.html', context=context)
  
class BookDetailView(View):
    def get(self, request, pk):
      book = Books.objects.get(pk=pk)
      context = {
        'book': book
      }
      return render(request, template_name='book/book_detail.html', context=context)
      
      
# class BookDetailView(View):
#     def get(self, request, pk):
#         book = get_object_or_404(Books, pk=pk)
#         context = {
#             'book': book
#         }
#         return render(request, 'book/book_detail.html', context)