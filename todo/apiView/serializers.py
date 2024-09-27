from rest_framework.serializers import ModelSerializer
from todo.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields=['title','description', 'active','id']

    def create(self, validated_data):
        print(type(validated_data))
        return Task.objects.create(**validated_data)
