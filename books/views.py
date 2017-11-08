from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, Borrowing
from books.forms import BookForm
from django.core.urlresolvers import reverse
from django.utils.formats import get_format
from datetime import datetime
from django.utils.dateformat import DateFormat

def index(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render(request, 'books/index.html', context)

def add_book(request):
    booksurl = request.build_absolute_uri(reverse('books:index'))
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        print (book_form.errors)
        if book_form.is_valid():
            book_ISBN = book_form.cleaned_data['ISBN']
            book_name = book_form.cleaned_data['name']
            book_description = book_form.cleaned_data['description']
            book_author = book_form.cleaned_data['author']
            book_publication_year = book_form.cleaned_data['publication_year']
            book_publisher = book_form.cleaned_data['publisher']
            book_page_count = book_form.cleaned_data['page_count']
            book_cover_URL = book_form.cleaned_data['cover_URL']
            new_book = Book(ISBN=book_ISBN, name=book_name, description=book_description, author=book_author, publication_year=book_publication_year, publisher=book_publisher, page_count=book_page_count, cover_URL=book_cover_URL)
            new_book.save()
            return HttpResponseRedirect('/')
    else:
        book_form = BookForm()
    return render(request, 'books/add_book.html', {'booksurl': booksurl, 'book_form': book_form})

def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'books/detail.html', {'book': book})

def borrow(request, book_id):
    detailurl = request.build_absolute_uri(reverse('books:detail', args=[book_id]))
    book = Book.objects.get(pk=book_id)
    book.borrowed = True
    book.save()
    date = DateFormat(datetime.now()).format(get_format('DATE_FORMAT'))
    new_borrowing = Borrowing(borrowing_date=date, book=book)
    new_borrowing.save()
    return render(request, 'books/detail.html', {'detailurl': detailurl, 'book': book})

def return_book(request, book_id):
    detailurl = request.build_absolute_uri(reverse('books:detail', args=[book_id]))
    book = Book.objects.get(pk=book_id)
    book.borrowed = False
    book.save()
    return render(request, 'books/detail.html', {'detailurl': detailurl, 'book': book})
