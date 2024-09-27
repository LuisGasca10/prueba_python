from rest_framework.serializers import ModelSerializer
from todo.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields=['title','description']

    def create(self, validated_data):
        print(validated_data)
        return Task.objects.create(**validated_data)
