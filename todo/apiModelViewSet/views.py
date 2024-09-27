from http import HTTPMethod

from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from todo.models import Task
from rest_framework import status
from todo.apiView.serializers import TaskSerializer


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=[HTTPMethod.POST], url_name='change-state-viewset', url_path='change')
    def changeState(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if (task.active):
            task.active = False
        else:
            task.active = True
        task.save()
        return Response(status=status.HTTP_200_OK, data="Se cambio de estado")