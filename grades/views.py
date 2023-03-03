from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Grade, Module
from .serializers import GradeSerializer, ModuleSerializer


class ModuleViewset(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)


class GradeViewset(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Grade.objects.filter(user=self.request.user)
