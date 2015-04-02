from django.shortcuts import render

from .models import Book

def index(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'books/index.html', context)
