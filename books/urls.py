from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^$', views.index, name='index'),
]
