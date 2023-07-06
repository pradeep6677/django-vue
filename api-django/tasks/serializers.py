from rest_framework import routers,serializers,viewsets
from .models import Task
class TaskSerializer(serializers.HyperlinkedModelSerializer):

    # def create(self, validated_data):
    #     # Once the request data has been validated, we can create a todo item instance in the database
    #     return Task.objects.create(
    #         text=validated_data.get('text')
    #     )

    # def update(self, instance, validated_data):
    #     # Once the request data has been validated, we can update the todo item instance in the database
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.save()
    #     return instance

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']