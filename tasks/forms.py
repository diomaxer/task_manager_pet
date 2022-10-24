from django import forms
from .models import Task, SimpleTask


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'head_task',
            'deadline',
        ]
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class SimpleTaskForm(forms.ModelForm):

    class Meta:
        model = SimpleTask
        fields = ['title']
