from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    ISBN = forms.CharField(max_length=150)
    book_name = forms.CharField(max_length=150)
    description = forms.CharField(max_length=500)
    book_author = forms.CharField(max_length=150)
    publication_year = forms.IntegerField(min_value=1000, max_value=2999)
    publisher = forms.CharField(max_length=150)
    page_count = forms.IntegerField(min_value=0, max_value=9999)

    class Meta:
        model = Book
        fields = ('ISBN', 'book_name', 'description', 'book_author', 'publication_year', 'publisher', 'page_count',)
