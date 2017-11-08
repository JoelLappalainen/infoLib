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

    def __unicode__(self):
        return self.name
