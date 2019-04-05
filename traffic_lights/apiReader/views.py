from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse
from django.http import JsonResponse
from apiReader.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from .models import Sensor
from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from apiReader.forms import RegistrationForm
from django.contrib.auth.models import User




def home(request):
    return render(request, 'extensions/home.html')

def profile(request):
    args = {'user': request.user}
    return render(request, 'extensions/profile.html', args)


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = RegistrationForm()
    return render(request, 'extensions/signup.html', {'form': form})

def edit_profile(request):
    if request.method =='POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'extensions/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def delete_profile(request, username):
    context = {}

    try:
        u = User.objects.get(username=username)
        u.delete()
        context['msg'] = 'The user is deleted.'       
    except User.DoesNotExist: 
        context['msg'] = 'User does not exist.'
    except Exception as e: 
        context['msg'] = e.message

    return render(request, 'extensions/delete_profile.html', context=context) 
  



#from .models import trafficDetector

def api(request):
    #response = requests.get('http://trafficlights.tampere.fi/api/v1/trafficAmount')
    response = requests.get('http://trafficlights.tampere.fi/api/v1/queueLength')
    detectorData = response.json()
    detectorData = detectorData['results']
    return render(request, 'extensions/trafficdata.html', {'detectorData': detectorData})


 # return render(request, 'extensions/trafficdata.html')

#def comment(request):
 #   if request.method == "POST":
  #      instance_text = Comment()
   #     instance_text.input = request.POST['textfield']
    #    instance_text.save()

#    text_list = Comment.objects.all()
 #   return render(request, "comment.html", {'text_list':text_list})
  
#@login_required  
#def sensor_list(request):  
#     if request.user.is_superuser:  
#         sensors = Sensor.objects.all()  
#     else:  
#         sensors = Sensor.objects.filter(user=request.user)  
#     return render(request, 'sensor_list.html', {  
#         'object_list': sensors  
#     })  
  
  
#@login_required  
#def sensor_create(request):  
#     form = SensorForm(request.POST or None)  
   
#     if form.is_valid():  
#         sensor = form.save(commit=False)  
#         sensor.user = request.user  
#         sensor.save()  
#         return redirect('apiReader:sensor_list')  
#     return render(request, 'sensor_form.html', {'form': form})  
  
  
#@login_required  
#def sensor_update(request, pk):  
#     if request.user.is_superuser:  
#         sensor = get_object_or_404(Sensor, pk=pk)  
#     else:  
#         sensor = get_object_or_404(Sensor, pk=pk, user=request.user)  
#     form = SensorForm(request.POST or None, instance=movies)  
#     if form.is_valid():  
#         form.save()  
#         return redirect('apiReader:sensor_list')  
#     return render(request, 'sensor_form.html', {'form': form})  
  
  
#@login_required  
#def sensor_delete(request, pk):  
#     if request.user.is_superuser:  
#         sensor = get_object_or_404(Sensor, pk=pk)  
#     else:  
#         sensor = get_object_or_404(Sensor, pk=pk, user=request.user)  
#     if request.method == 'POST':  
#         sensor.delete()  
#         return redirect('apiReader:sensor_list')  
#     return render(request, 'confirm_delete.html', {'object': sensor})