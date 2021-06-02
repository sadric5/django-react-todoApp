from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = 'id', 'author', 'title', 'description', 'create_at', 'completed'
        # fields = '__all__'
