from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=150)
    publication_year = models.IntegerField(default=0)
    publisher = models.CharField(max_length=150)
    page_count = models.IntegerField(default=0)
    cover_URL = models.URLField(max_length=250)
    #temporarily
    borrowed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Borrowing(models.Model):
    borrowing_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    returning_date = models.DateTimeField(null=True, blank=True)
