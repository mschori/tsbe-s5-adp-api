from rest_framework import generics, views
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, SignupSerializer, SigninSerializer


class SignupView(generics.CreateAPIView):
    """
    View for Signup.
    """
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        create_state = self.create(request, *args, **kwargs)
        if create_state.status_code != 201:
            return create_state
        user = User.objects.get(email=request.data['email'])
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'access_token': str(tokens.access_token),
                'refresh_token': str(tokens),
                'user': UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )


class SigninView(views.APIView):
    serializer_class = SigninSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'access_token': str(tokens.access_token),
                'refresh_token': str(tokens),
                'user': UserSerializer(user).data
            },
            status=status.HTTP_200_OK
        )
