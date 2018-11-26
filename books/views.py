from django.shortcuts import render, redirect
from books.models import Book
# from books.forms import SuggestionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User, AbstractUser


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
    python_books = Book.objects.filter(python=True)
    return render(request, 'python.html', {
        'python_books': python_books,
    })

def css(request):
    css_books = Book.objects.filter(css=True)
    return render(request, 'css.html', {
        'css_books': css_books,
    })

def html(request):
    html_books = Book.objects.filter(html=True)
    return render(request, 'html.html', {
        'html_books': html_books,
    })

def javascript(request):
    javascript_books = Book.objects.filter(javascript=True)
    return render(request, 'javascript.html', {
        'javascript_books': javascript_books,
    })
 
# @login_required
# def book_suggestion(request):
#     current_user = request.user
#     if request.POST:
#         form = SuggestionForm(request.POST, instance=current_user)
#         if form.is_valid():
#             suggestion = form.save(commit=True)
#             suggestion.save()
#             return redirect('book_list')
#         else:
#             form = SuggestionForm(instance=current_user)

#     return render(request, "book_suggestion.html", {
#         "form": form,
        


#     })
