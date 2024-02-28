from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello everyone!!")

def samiksha(request):
    return HttpResponse("Hello Samiksha")