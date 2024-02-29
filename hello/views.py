from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def samiksha(request):
    return HttpResponse("Hello Samiksha")

#parameterised palceholder to display dynamic greeting when the name is mentioned in the url
def greet(request, name):
    return HttpResponse(f"Hello,{name.capitalize()}!")