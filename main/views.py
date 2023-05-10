import json
import requests
from django.http import *
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import PrepodForm, TaskForm
from .models import Task
from .viewsModels import TableViewModel

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'main page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "form invalid"

    form = TaskForm()
    conttext = {
        'form': form
    }
    return render(request, 'main/create.html', conttext)

def table(request):
    vm = TableViewModel()
    form_class = PrepodForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            oneName = form.cleaned_data['name']
            oneNamelist = set(oneName.split())
            start = form.cleaned_data['date']
            allTypeList = []
            for searchQuery in oneNamelist:
                result = vm.get_search(query=searchQuery)
                for item in result:
                    id = item['id']
                    type = item['type']
                    schedule = vm.get_schedule(type, id, start, end=start)
                    if (item["type"] != "lecture") and (item["type"] != "auditorium" and (item["type"] != "building")):
                        allTypeList.append({"type": item["type"], "description": item["label"], "list": schedule})
            form.eventsData = allTypeList
        else:
            form = PrepodForm()
    return render(request, 'main/table.html', {'form': form})


def tests(request):
    return render(request, 'main/tests.html')
