from django.shortcuts import render

from .models import Task
from .forms import TaskForm


def task_view(request):
    tasks = Task.objects.filter(done=False)
    done_tasks = Task.objects.filter(done=True)
    context = {
        'tasks': tasks,
        'done_tasks': done_tasks
    }
    return render(request, 'index.html', context=context)


def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(
        initial={
            'title': task.title,
            'description': task.description,
            'head_task': task.head_task,
            'deadline': task.deadline,
        })
    print(task.deadline)
    if request.method == 'POST':
        if 'update' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                task.title = form.cleaned_data['title']
                task.description = form.cleaned_data['description']
                task.head_task = form.cleaned_data['head_task']
                task.deadline = form.cleaned_data['deadline']
                task.save()
                print(form.cleaned_data['deadline'])
                return render(request, 'task_detail.html', {'task': task, 'form': form})
        elif 'done' in request.POST:
            task.done = not task.done
            task.save()
            return render(request, 'task_detail.html', {'task': task, 'form': form})
    return render(request, 'task_detail.html', {'task': task, 'form': form})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                head_task=form.cleaned_data['head_task'],
                user=request.user
            )
            form.clean()
            render(request, 'task_create.html', {'form': form})
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'task_create.html', context)
