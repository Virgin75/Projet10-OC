from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from issuetracker.views import ListCreateProject, ListCreateProjectContributor, RetrieveUpdateDestroyProject, DestroyContributor, ListCreateIssue, UpdateDestroyIssue


urlpatterns = [
    path('projects/<uuid:project_id>/', RetrieveUpdateDestroyProject.as_view()),
    path('projects/', ListCreateProject.as_view()),
    path('projects/<uuid:project_id>/users/', ListCreateProjectContributor.as_view()),
    path('projects/<uuid:project_id>/users/<int:user_id>/', DestroyContributor.as_view()),
    path('projects/<uuid:project_id>/issues/', ListCreateIssue.as_view()),
    path('projects/<uuid:project_id>/issues/<int:id>/', UpdateDestroyIssue.as_view()),
]
