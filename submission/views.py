from django.shortcuts import render
from submission.models import Track, Submission
from  .filters import SubmissionFilter
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url= "/login/")
def show_submission(request):
    global submission_filter
    track_data = Track.objects.all()
    submission_data = Submission.objects.all()
    submission_filter = SubmissionFilter(request.GET, queryset=submission_data)
    context = {'track' : track_data,
                'submission_filter' : submission_filter}
    return render(request, "submission.html", context)

@login_required(login_url= "/login/")
def show_details_by_id(request, id):
    track_data = Track.objects.filter(id=id)
    submission_data = Submission.objects.filter(id=id)
    context = {'track' : track_data,
                'submission' : submission_data}
    return render(request, "details.html", context)

@login_required(login_url= "/login/")
def show_json(request):
    return HttpResponse(serializers.serialize("json", submission_filter.qs), content_type="application/json")