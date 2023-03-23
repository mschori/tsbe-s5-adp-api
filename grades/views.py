from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Grade, Module
from .serializers import GradeSerializer, ModuleSerializer


class ModuleViewset(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Module.objects.filter(user=self.request.user)


class GradeViewset(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Grade.objects.filter(module__user=self.request.user)
