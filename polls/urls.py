from django.conf.urls import url

from . import views

urlPatterns = [
    url(r'^$', views.index, name = 'index'),
]