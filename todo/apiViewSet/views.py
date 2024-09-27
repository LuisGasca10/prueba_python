from http import HTTPMethod

from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from todo.models import Task
from rest_framework import status
from todo.apiView.serializers import TaskSerializer


class TasksViewSet(ViewSet):
    def list(self, request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)

    def retrieve(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        try:
            serializer = TaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        # Obtiene el objeto Task que deseas actualizar
        task = get_object_or_404(Task, pk=pk)

        # Crea el serializer con los datos entrantes, usando partial=True
        serializer = TaskSerializer(task, data=request.data, partial=True)

        # Verifica si el serializer es válido
        if serializer.is_valid():
            serializer.save()  # Guarda los cambios en el objeto
            return Response(serializer.data)  # Retorna los datos actualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=204,data="Eliminado correctamente")

    @action(detail=True ,methods=[HTTPMethod.POST],url_name='change-state-viewset',url_path='change')
    def changeState(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        if(task.active):
            task.active=False
        else:
            task.active=True
        task.save()
        return Response(status=status.HTTP_200_OK, data="Se cambio de estado")



