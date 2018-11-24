from django.shortcuts import render, redirect
from books.models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books,
    })

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })

def python(request):
    category = Book.get_categories
    return render(request, 'python.html', {
        'category': category
    })
 