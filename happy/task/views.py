from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

task= []
priority= []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="new task")
 #   priority = forms.IntegerField(label="priority", min_value=1, max_value=5)
    
# Create your views here.
def index(request):
    return render(request,"task/index.html", {
        "task": task
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            task.append(task)
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html", {
                "form": form
            })
    
    return render(request, "task/add.html", {
        "form": NewTaskForm()
    })