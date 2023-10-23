from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Category, Task, SubTask


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(CurrentUserDefault())
    )

    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(CurrentUserDefault())
    )

    class Meta:
        model = Category
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
