from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(default=0)
    ISBN = models.CharField(max_length=150)
    book_name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    book_author = models.CharField(max_length=150)
    publication_year = models.IntegerField(default=0)
    publisher = models.CharField(max_length=150)
    page_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.book_name
