from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from todo.urls import router as todo_router
from users import views as user_views

router = routers.DefaultRouter(trailing_slash=False)
router.registry.extend(todo_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup', user_views.SignupView.as_view(), name='signup'),
    path('api/signin', user_views.SigninView.as_view(), name='signin'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
]
