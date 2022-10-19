from django.urls import path
from tasks.views import task_detail, task_create, task_detail_update


urlpatterns = [
    path('create', task_create, name='task-create'),
    path('<int:pk>', task_detail, name='task-detail'),
    path('<int:pk>/update', task_detail_update, name='task-detail-update'),
]