from rest_framework.routers import DefaultRouter
from todo.apiModelViewSet.views import TaskModelViewSet
router = DefaultRouter()

router.register('tasks',TaskModelViewSet,basename="task-model-viewset")