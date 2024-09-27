from django.urls import path
from .views import TaskApiView,TaskDetailView,changeState

urlpatterns = [
    path('tasks/', TaskApiView.as_view(), name='task-list'),  # Ruta para la lista de tareas
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # Ruta para el detalle de tarea
    path('tasks/<int:pk>/change',changeState,name="task-change")
]