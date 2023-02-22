from django.urls import path
from .views import TaskListView, TaskDetailView, CreateTask

todo_patterns = [
    path('tasks/', TaskListView.as_view(), name = 'tastlist'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name = 'tastdetail'),
    path('tasks/create/', CreateTask.as_view(), name='createtask'),
]