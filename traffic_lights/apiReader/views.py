from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse
from django.http import JsonResponse
from apiReader.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



#from .models import trafficDetector

#def api(request):
 #   response = requests.get('http://trafficlights.tampere.fi/api/v1/trafficAmount')
  #  detectorData = response.json()
   # return render(request, 'comment.html', {'detectorData': detectorData})

#def comment(request):
 #   if request.method == "POST":
  #      instance_text = Comment()
   #     instance_text.input = request.POST['textfield']
    #    instance_text.save()

#    text_list = Comment.objects.all()
 #   return render(request, "comment.html", {'text_list':text_list})

def home(request):
    return render(request, 'extensions/home.html')

def profile(request):
    return render(request, 'extensions/profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = UserCreationForm()
    return render(request, 'extensions/signup.html', {'form': form})

