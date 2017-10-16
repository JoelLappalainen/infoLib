from django.shortcuts import render, redirect
from .models import Book

def index(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render(request, 'books/index.html', context)
