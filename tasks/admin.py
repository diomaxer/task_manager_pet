from django.contrib import admin
from tasks.models import Task, SimpleTask


admin.site.register(Task)
admin.site.register(SimpleTask)