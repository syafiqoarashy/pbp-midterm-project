from django.urls import path
from submission.views import *

app_name = 'submission'

urlpatterns = [
    path('', show_submission, name='show_submission'),
    path('details/<str:id>', show_details_by_id, name='show_details_by_id'),
    path('json/', show_json, name='show_json'),
]