from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todos')
