from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Model-Serializer for Users.
    """

    class Meta:
        model = User
        exclude = ['password', 'user_permissions']
