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
    if request.method == 'POST':
        form = PrepodForm(request.POST)
        if form.is_valid():
            start='2021.11.16'
            finish='2021.11.16'
            response = requests.get('https://rasp.omgtu.ru/api/schedule/person/'+form.cleaned_data['id'], params={
                "start": start,
                "finish": finish,
                "lng": 1
                })
            form = response.json()
        else:
            form = PrepodForm()
    return render(request,'main/table.html', {'form': form})