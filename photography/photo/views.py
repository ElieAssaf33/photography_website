from django.shortcuts import render
from django.http import HttpRequest
from . import models

def index(request:HttpRequest):
    context = {'photos' : models.Photos.objects}
    return render(request,'photo/index.html', context)

def portfolio(request:HttpRequest):
    return render(request,'photo/portfolio.html', context={})

def prices(request:HttpRequest):
    return render(request,'photo/prices.html', context={})

def contacts(request:HttpRequest):
    return render(request,'photo/contacts.html', context={})



