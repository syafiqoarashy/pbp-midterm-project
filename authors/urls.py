from django.urls import path

from authors.views import *

app_name='authors'

urlpatterns = [
    path('', show_authors, name='show_authors'),
    path('authdetails/<str:id>', show_details, name='show_details'),
    path('json/', show_json, name='show_json'),
]