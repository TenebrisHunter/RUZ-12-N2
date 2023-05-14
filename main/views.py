
from django.shortcuts import render, redirect

from .forms import PrepodForm, TaskForm
from .models import Task
from .utils import sort_dict
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
    if request.method == 'POST':

        form = PrepodForm(request.POST)

        if form.is_valid():
            one_name = form.cleaned_data['name']
            one_name_list = set(one_name.split())
            start = form.cleaned_data['date']
            dates = set()
            pairs = set()

            all_schedule = {}
            for search_query in one_name_list:
                objects = vm.get_search(query=search_query)
                for item in objects:
                    schedule = vm.get_schedule(item['type'], item['id'], start, end=start)
                    if item["type"] not in ("lecture", "building"):
                        for pair in schedule:

                            if pair['date'] not in all_schedule:
                                all_schedule[pair['date']] = {}
                                dates.add(pair['date'])

                            item_time = f"{pair['beginLesson']} - {pair['endLesson']}"
                            if item_time not in all_schedule[pair['date']]:
                                all_schedule[pair['date']][item_time] = {}
                                pairs.add(item_time)

                            if search_query not in all_schedule[pair['date']][item_time]:
                                all_schedule[pair['date']][item_time][search_query] = []

                            if pair not in all_schedule[pair['date']][item_time][search_query]:
                                same = list(filter(
                                    lambda x: x["kindOfWork"] == pair["kindOfWork"] and x["subGroup"] == pair["subGroup"],
                                    all_schedule[pair['date']][item_time][search_query]
                                ))
                                if same:
                                    same_p = same[0]
                                    same_p["listOfLecturers"].extend(pair["listOfLecturers"])
                                else:
                                    all_schedule[pair['date']][item_time][search_query].append(pair)

            all_schedule = sort_dict(all_schedule)
            form.eventsData = {'schedule': all_schedule, 'names': one_name_list}

    else:
        form = PrepodForm()
    return render(request, 'main/table.html', {'form': form})


def tests(request):
    return render(request, 'main/tests.html')
