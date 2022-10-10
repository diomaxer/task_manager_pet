from django.shortcuts import render

from .models import Task
from .forms import TaskForm


def task_view(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                # description=form.cleaned_data['descruption'],
                user=request.user
            )
            form.clean()
            render(request, 'index.html', {'form': form})
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'index.html', context)


def task_detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task_detail.html', {'task': task})