from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'modules', views.ModuleViewset, basename='modules')
router.register(r'grades', views.GradeViewset, basename='grades')
