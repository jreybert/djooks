from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /books/
    url(r'^$', views.index, name='index'),
    # ex: /books/list/
    #url(r'^list/$', views.list, name='list'),
]

