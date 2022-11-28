from django.urls import path
from .views import category, show_json_category

app_name = 'parallel_sessions'

urlpatterns = [
    path('', category, name='category'),
    path('json_category/', show_json_category, name="json_category"),
    
]