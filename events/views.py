import datetime
from django.shortcuts import render
from events.models import EventsGeneral, EventsParallel
from django.http import HttpResponse
from django.core import serializers
from speakers.models import Speakers
from submission.models import Track
from django.contrib.auth.decorators import login_required

@login_required(login_url= "/login/")
def show_events_general(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 22))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 22))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral.html", context)

@login_required(login_url= "/login/")
def show_events_general23(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 23))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 23))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral23.html", context)

@login_required(login_url= "/login/")
def show_events_general24(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 24))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 24))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral24.html", context)

@login_required(login_url= "/login/")
def show_events_general25(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 25))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 25))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral25.html", context)

@login_required(login_url= "/login/")
def show_json(request):
    data = EventsGeneral.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url= "/login/")
def show_parallel_json(request):
    data = EventsParallel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url= "/login/")
def show_tracks_json(request):
    data = Track.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url= "/login/")
def show_events_ajax(request):
    return render(request, "generalajax.html")

@login_required(login_url= "/login/")
def show_speakers_json(request):
    data = Speakers.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")