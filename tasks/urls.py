from django.urls import path
from tasks.views import task_detail, task_create


urlpatterns = [
    path('create', task_create, name='task-create'),
    path('<int:pk>', task_detail, name='task-detail'),
]