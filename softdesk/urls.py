from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin
from issuetracker.views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^user/', include(('users.urls', 'users'), namespace='users')),
]
