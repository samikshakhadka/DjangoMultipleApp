from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value= 0 , max_value= 10)

# Create your views here.

def index(request):
    #storing data inside user session to implement session storage
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]

    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse ("tasks:index")) #reverse engineer url to redirect back to dashboard after adding new task
        else:
            return render(request, "tasks/index.html",
                          {
                              'form': form
                          })
    return render(request, "tasks/add.html" ,
                  {
                      "form" : NewTaskForm()
                  })