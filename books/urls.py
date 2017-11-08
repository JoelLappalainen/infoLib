from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^return/(?P<book_id>[0-9]+)/$', views.return_book, name='return'),
    url(r'^borrow/(?P<book_id>[0-9]+)/$', views.borrow, name='borrow'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^$', views.index, name='index'),
]
