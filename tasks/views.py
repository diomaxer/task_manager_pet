from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


def change_task_status(request):
    task = Task.objects.get(id=list(request.POST.keys())[-1])
    task.done = not task.done
    task.save()


def task_view(request):
    if request.user.is_anonymous:
        tasks = None
    else:
        tasks = Task.objects.filter(user=request.user, done=False).order_by('-id')
    if request.method == 'POST':
        change_task_status(request)
    context = {
        'tasks': tasks,
    }
    return render(request, 'task/index.html', context=context)


@login_required
def task_done(request):
    tasks = Task.objects.filter(user=request.user, done=True).order_by('-id')
    if request.method == 'POST':
        change_task_status(request)
    context = {
        'tasks': tasks,
    }
    return render(request, 'task/index.html', context=context)


@login_required
def task_detail(request, pk):
    # task = Task.objects.get(id=pk, user=request.user)
    task = get_object_or_404(Task, id=pk, user=request.user)
    child_tasks = Task.objects.filter(head_task=task)
    print(child_tasks)
    context = {
        'task': task,
        'child_tasks': child_tasks,
    }
    if request.method == 'POST':
        task.done = not task.done
        task.save()
        return render(request, 'task/task_detail.html', context)
    return render(request, 'task/task_detail.html', context)


@login_required
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
    return render(request, 'task/task_create.html', context)


@login_required
def task_detail_update(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
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
    return render(request, 'task/task_detail_update.html', {'task': task, 'form': form})