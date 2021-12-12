from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Task
from .forms import PrepodForm, TaskForm
import json
import requests
from django.http import *

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main/index.html', {'title': 'main page', 'tasks': tasks})

def about(request):
    return render(request,'main/about.html')

def create(request):
    error=""
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
    return render(request,'main/create.html', conttext)

def table(request):
    form_class = PrepodForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            start=form.cleaned_data['date']
            responseFIO  = requests.get('https://rasp.omgtu.ru/api/search?term='+form.cleaned_data['name']+'&type=person')
            responseFIOJSON = responseFIO.json()
            nameID = responseFIOJSON[0]['id']
            response = requests.get('https://rasp.omgtu.ru/api/schedule/person/'+str(nameID), params={
                "start": start,
                "finish": start,
                "lng": 1
                })
            form = response.json()
        else:
            form = PrepodForm()
    return render(request,'main/table.html', { 'form': form })

def tests(request):
    return render(request, 'main/tests.html')
