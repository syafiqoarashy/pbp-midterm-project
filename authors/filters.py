import django_filters
from .models import *

class AuthorsFilter(django_filters.FilterSet):
    class Meta:
        model = Authors
        fields = {'full_name':['icontains']}