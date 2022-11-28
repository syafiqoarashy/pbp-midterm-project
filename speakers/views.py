from django.shortcuts import render
from speakers.models import Speakers
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = 'show_speakers.html'

class SearchResultsView(ListView):
    model = Speakers
    template_name = 'search_speakers.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Speakers.objects.filter(name__icontains=query)
        return object_list

@login_required(login_url= "/login/")
def show_speakers(request):
    data_speakers = Speakers.objects.all()
    data_speakers_plenary = Speakers.objects.all().filter(type="plenary")
    data_speakers_keynote = Speakers.objects.all().filter(type="keynote")
    data_speakers_invited = Speakers.objects.all().filter(type="invited")
    
    context = {
    'list_speakers': data_speakers,
    'list_speakers_plenary': data_speakers_plenary,
    'list_speakers_keynote': data_speakers_keynote,
    'list_speakers_invited': data_speakers_invited
    }
    return render(request, 'show_speakers.html', context)

@login_required(login_url= "/login/")
def show_speakers_info(request, id): # detailed info of speaker
    data_speakers = Speakers.objects.filter(pk=id)
    context = {
        'speakers_info': data_speakers
    }
    return render(request, 'show_speakers_info.html', context)

@login_required(login_url= "/login/")
def show_json(request):
    data = Speakers.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")