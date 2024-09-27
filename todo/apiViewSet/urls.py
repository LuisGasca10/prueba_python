
from rest_framework.routers import DefaultRouter
from todo.apiViewSet.views import TasksViewSet
router = DefaultRouter()

router.register('tasks',TasksViewSet,basename="task-viewset")
