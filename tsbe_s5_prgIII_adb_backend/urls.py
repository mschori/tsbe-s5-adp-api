from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from todo.urls import router as todo_router
from users.urls import router as user_router

router = routers.DefaultRouter(trailing_slash=False)
router.registry.extend(user_router.registry)
router.registry.extend(todo_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
]
