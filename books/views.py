from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from books.models import Book, Borrowing, Review
from books.forms import BookForm, UserForm, ReviewForm
from django.core.urlresolvers import reverse
from django.utils.formats import get_format
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.contrib.auth.decorators import login_required


def index(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render(request, 'books/index.html', context)


@login_required
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
            new_book = Book(ISBN=book_ISBN, name=book_name, description=book_description, author=book_author,
                            publication_year=book_publication_year, publisher=book_publisher, page_count=book_page_count, cover_URL=book_cover_URL)
            new_book.save()
            return HttpResponseRedirect('/')
    else:
        book_form = BookForm()
    return render(request, 'books/add_book.html', {'booksurl': booksurl, 'book_form': book_form})


def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        all_borrowings = Borrowing.objects.all()
        all_reviews = Review.objects.all()
    except Book.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'books/detail.html', {'book': book, 'all_borrowings': all_borrowings, 'all_reviews': all_reviews})


def profile(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        all_borrowings = Borrowing.objects.all()
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'profile.html', {'user': user, 'all_borrowings': all_borrowings})


@login_required
def borrow(request, book_id, user_id):
    detailurl = request.build_absolute_uri(
        reverse('books:detail', args=[book_id]))
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=user_id)
    book.borrowed = True
    book.borrower = user
    book.status = 'o'
    book.save()
    date = DateFormat(datetime.now()).format(get_format('DATE_FORMAT'))
    new_borrowing = Borrowing(borrowing_date=date, book=book, borrower=user)
    new_borrowing.save()
    # return render(request, 'books/detail.html', {'detailurl': detailurl, 'book': book})
    return HttpResponseRedirect('/')


@login_required
def return_book(request, book_id):
    detailurl = request.build_absolute_uri(
        reverse('books:detail', args=[book_id]))
    book = Book.objects.get(pk=book_id)
    book.borrowed = False
    book.borrower = None
    book.status = 'a'
    book.save()
    # return render(request, 'books/detail.html', {'detailurl': detailurl, 'book': book})
    return HttpResponseRedirect('/')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print (user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})


def reviews(request, book_id, user_id):
    detailurl = request.build_absolute_uri(
        reverse('books:detail', args=[book_id]))
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        print (review_form.errors)
        if review_form.is_valid():
            date = DateFormat(datetime.now()).format(get_format('DATE_FORMAT'))
            review = review_form.cleaned_data['review']
            rating = review_form.cleaned_data['rating']
            book = Book.objects.get(pk=book_id)
            reviewer = request.user
            new_review = Review(
                date=date, review=review, rating=rating, reviewed_book=book, reviewer=reviewer)
            new_review.save()
            return HttpResponseRedirect(detailurl)
    else:
        review_form = ReviewForm()
    return render(request, 'books/review_book.html', {'detailurl': detailurl, 'review': review_form})
