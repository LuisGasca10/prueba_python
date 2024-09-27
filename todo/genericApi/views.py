from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework.response import Response

from todo.models import Task
from todo.apiView.serializers import TaskSerializer

class TasksGenericView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class TaskChangeState(UpdateAPIView):
    serializer_class = TaskSerializer
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        task = get_object_or_404(Task,pk=pk)
        if(task.active):
            task.active=False
        else:
            task.active=True
        task.save()
        return Response(status=status.HTTP_206_PARTIAL_CONTENT,data="Se cambio de estado")
