from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def samiksha(request):
    return HttpResponse("Hello Samiksha")

#parameterised palceholder to display dynamic greeting when the name is mentioned in the url
# def greet(request, name):
#     return HttpResponse(f"Hello,{name.capitalize()}!")


#ginga logic can be used to rendera variable inside the html template, therfore we pass an extra context or variable
def greet(request, name):
    return render(request,"hello/greet.html",
                  {
                      "name": name.capitalize()  #this is context
                  } 
                 )