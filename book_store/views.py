
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Book

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'book_store/book_list.html', {'books': books})

from django.http import HttpResponse

def user_home(request):
    return HttpResponse("Welcome to the User Page!")

