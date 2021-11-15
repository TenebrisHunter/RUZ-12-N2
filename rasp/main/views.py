from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm
import json
from django.http import JsonResponse

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
    data = {
        "values": [
            'hello',
            'rwo',
            'shahs',
            'next',
            'ddddd'
        ]
    }
    return render(request,'main/table.html',data)