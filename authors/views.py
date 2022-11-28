from django.shortcuts import render
from .filters import AuthorsFilter
from .models import *
from django.http import HttpResponse
from django.core import serializers
from submission.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url= "/login/")
def show_authors(request):
    global authors_filter
    authors_data = Authors.objects.all()
    authors_filter = AuthorsFilter(request.GET, queryset=authors_data)
    context = {
        'authors' : authors_data,
        'authors_filter':authors_filter
    }
    return render(request,"authors.html",context)

@login_required(login_url= "/login/")
def show_details(request,id):
    authors_data = Authors.objects.filter(id=id)
    submission_data = Submission.objects.filter(id=authors_data[0].submission_id)
    context = {
        'name' : authors_data,
        'submission' : submission_data
    }
    return render(request, "authdetails.html", context)

@login_required(login_url= "/login/")
def show_json(request):
    return HttpResponse(serializers.serialize("json", authors_filter.qs), content_type="application/json")