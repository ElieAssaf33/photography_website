from django.shortcuts import render
from django.http import HttpRequest
from . import models

def index(request:HttpRequest):
    context = {'photos' : models.Photos.objects}
    return render(request,'photo/index.html', context)