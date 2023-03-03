from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Model-Serializer for Users.
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'firstname', 'lastname', 'dated_joined', 'last_login')


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        allow_blank=False,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ('password', 'email', 'firstname', 'lastname')
        extra_kwargs = {
            'firstname': {'required': True},
            'lastname': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            is_active=True
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
