from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book
from books.forms import BookForm
from django.core.urlresolvers import reverse
from django.utils.formats import get_format

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
            print ("valid")
            book_ISBN = book_form.cleaned_data['ISBN']
            book_name = book_form.cleaned_data['book_name']
            book_description = book_form.cleaned_data['description']
            book_author = book_form.cleaned_data['book_author']
            book_publication_year = book_form.cleaned_data['publication_year']
            book_publisher = book_form.cleaned_data['publisher']
            book_page_count = book_form.cleaned_data['page_count']
            new_book = Book(ISBN=book_ISBN, book_name=book_name, description=book_description, book_author=book_author, publication_year=book_publication_year, publisher=book_publisher, page_count=book_page_count)
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
