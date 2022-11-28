from django.shortcuts import render
from .models import Tracks
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url= "/login/")
def category(request) :
    tracks = Tracks.objects.all()
    context = {
        'tracks': tracks,
    }
    return render(request, 'category.html', context)

@login_required(login_url= "/login/")
def show_json_category(request):
    data = Tracks.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

