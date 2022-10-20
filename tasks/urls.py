from django.urls import path
from tasks.views import task_detail, task_create, task_detail_update, task_done


urlpatterns = [
    path('done', task_done, name='task-done'),
    path('create', task_create, name='task-create'),
    path('<int:pk>', task_detail, name='task-detail'),
    path('<int:pk>/update', task_detail_update, name='task-detail-update'),
]