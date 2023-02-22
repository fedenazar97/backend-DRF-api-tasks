from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics

# Create your views here.

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
        

class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer
