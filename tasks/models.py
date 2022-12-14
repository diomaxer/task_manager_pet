from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    head_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SimpleTask(models.Model):
    title = models.CharField(max_length=100) # Заменить на mini_task
    done = models.BooleanField(default=False)
    head_task = models.ForeignKey(Task, on_delete=models.CASCADE)


