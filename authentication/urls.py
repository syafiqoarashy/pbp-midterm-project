from django.urls import path
from authentication.views import login

app_name = 'auth'

urlpatterns = [
    path('', login, name='login'),
]