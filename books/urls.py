from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^(?P<book_id>[0-9]+)/return/$', views.return_book, name='return'),
    url(r'^(?P<book_id>[0-9]+)/(?P<user_id>[0-9]+)/borrow/$', views.borrow, name='borrow'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^reviews/(?P<book_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.reviews, name='reviews'),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^search/', views.search, name='search'),
    url(r'^$', views.index, name='index'),
    url(r'^adminpage/', views.adminpage, name="adminpage"),
    url(r'^delete/(?P<book_id>[0-9]+)/$', views.delete_book, name='delete'),

    # todo: 'user' app for these?
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name="profile"),
    url(r'^register/', views.register, name="register"),
]
