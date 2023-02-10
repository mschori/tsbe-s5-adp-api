from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.urls import router as users_router

router = routers.DefaultRouter()
router.registry.extend(users_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
