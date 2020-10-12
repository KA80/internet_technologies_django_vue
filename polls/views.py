from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'polls/index.html', {'title': 'main page', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/polls')
        else:
            error = "incorrect form"

    form = TaskForm()
    ctx = {
        'form': form,
        'error': error
    }
    return render(request, 'polls/create.html', ctx)
