from django.shortcuts import render, redirect
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
    context = {
        'form': form
    }
    return render(request,'main/create.html', context)


def table(request):
    return render(request,'main/table.html')

def json_r(request):
    with open('data.json', 'r') as file:
        data = json.load(file)

def profile(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)