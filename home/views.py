from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from home.models import Testimonial
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

@login_required(login_url='/login/')
def landing_logged(request):
    testimonials = Testimonial.objects.all()
    context = {
        'user' : request.user,
        'items': testimonials,
    }   
    return render(request, "index2.html", context)

def landing(request):
    testimonials = Testimonial.objects.all()
    context = {
        'user' : request.user,
        'items': testimonials,
    }   
    return render(request, "index.html", context)

def render_test(request):
    testimonials = Testimonial.objects.all()
    context = {
        'user' : request.user,
        'items': testimonials,
    }   
    return render(request, "test_index.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:landing_logged')
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('home:login')

    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/login/')
def create_testimonial(request):
    if request.method == "POST":
        username = request.POST.get('username')
        content = request.POST.get('content')
        institute = request.POST.get('institute')
        if content != "" and username != "" and institute != "":
            data = Testimonial.objects.create(username=username, content=content, institute=institute)
            return JsonResponse({
                    "pk": data.id,
                    "fields": {
                        "username": data.username,
                        "content": data.content,
                        "institute": data.institute,
                    },
                },
                status=200,
            )
        else:
            messages.info(request, 'Please fill the username/content/institute!')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('home:login')

def show_data_json(request):
    data = Testimonial.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")