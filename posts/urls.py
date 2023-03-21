from sys import path_hooks
from typing import Pattern
from django import urls
from django.urls import path #
from . import views#
from django.urls.resolvers import URLPattern#

urlpatterns =[
    
    path('', views.index, name='index'),
    path('upload_csv', views.upload_file, name='upload_csv')
   
]
