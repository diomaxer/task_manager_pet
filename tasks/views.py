from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


def task_view(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        print(list(request.POST.keys())[-1])
        task = Task.objects.get(id=list(request.POST.keys())[-1])
        task.done = not task.done
        task.save()
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context=context)


def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.done = not task.done
        task.save()
        return render(request, 'task_detail.html', {'task': task})
    return render(request, 'task_detail.html', {'task': task})


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
            return redirect('home')
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'task_create.html', context)


def task_detail_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(
        initial={
            'title': task.title,
            'description': task.description,
            'head_task': task.head_task,
            'deadline': task.deadline,
        })
    if request.method == 'POST':
        if 'update' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                task.title = form.cleaned_data['title']
                task.description = form.cleaned_data['description']
                task.head_task = form.cleaned_data['head_task']
                task.deadline = form.cleaned_data['deadline']
                task.save()
                return redirect('task-detail', pk=pk)
    return render(request, 'task_detail_update.html', {'task': task, 'form': form})