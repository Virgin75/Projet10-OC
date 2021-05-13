from django.conf.urls import url
from django.urls import path, include
from users.views import CreateUserAPIView, LogInUserAPIView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('viewset/', include(router.urls)),
    url(r'^signup/$', CreateUserAPIView.as_view()),
    url(r'^login/$', LogInUserAPIView.as_view()),
]
