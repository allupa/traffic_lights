from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from django.http import JsonResponse
from apiReader.models import *


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