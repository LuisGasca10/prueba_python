from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TaskSerializer
from todo.models import Task
from rest_framework.decorators import api_view

class TaskApiView(APIView):
    def get(self,request):
        #print(bool(request.query_params.get('activated')))
        data=Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)


    def post(self,request):
        # print('POST ACCIONADO')
        # print(request.data)
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)




class TaskDetailView(APIView):

    def get(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self,request,pk):
        try:
            task = get_object_or_404(Task, pk=pk)
            task.delete()
            return Response(status=status.HTTP_200_OK, data="Se elimino correctamente")
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,data="Esta tarea no existe")


    # def post(self, request, pk):
    #     task = get_object_or_404(Task, pk=pk)
    #     if(task.active):
    #         task.active=False
    #     else:
    #         task.active = True
    #     task.save()
    #     return Response(status=status.HTTP_200_OK, data="Se cambio de estado")

@api_view(['POST'])
def changeState(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if(task.active):
        task.active=False
    else:
        task.active = True
    task.save()
    return Response(status=status.HTTP_200_OK, data="Se cambio de estado")