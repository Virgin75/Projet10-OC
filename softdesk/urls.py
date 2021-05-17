from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/', include(('users.urls', 'users'), namespace='users')),
    url('', include(('issuetracker.urls', 'issuetracker'),
                    namespace='issuetracker')),
]
