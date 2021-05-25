from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^v1/user/', include(('users.urls', 'users'), namespace='users')),
    url('v1/', include(('issuetracker.urls', 'issuetracker'),
                       namespace='issuetracker')),
]
