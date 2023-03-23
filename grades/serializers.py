from rest_framework import serializers

from .models import Module, Grade


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        exclude = ('user',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class GradeSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True)
    module_pk = serializers.PrimaryKeyRelatedField(
        queryset=Module.objects.all(),
        write_only=True,
        source='module'
    )

    class Meta:
        model = Grade
        fields = '__all__'

    def validate_module_pk(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('You do not own this module.')
        return value
