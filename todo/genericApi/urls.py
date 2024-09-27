from django.urls import path

from .views import TasksGenericView,TaskGenericView,TaskChangeState

urlpatterns =[
    path('tasks/',TasksGenericView.as_view(),name='tasks-generic'),
    path('tasks/<int:pk>/',TaskGenericView.as_view(),name='task-generic'),
    path('tasks/<int:pk>/change',TaskChangeState.as_view(),name='change-generic')
]