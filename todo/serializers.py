from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['user']

    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)
