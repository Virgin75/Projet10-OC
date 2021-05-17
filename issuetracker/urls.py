from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from issuetracker.views import ListCreateProject, ListCreateProjectContributor, RetrieveUpdateDestroyProject


urlpatterns = [
    path('projects/<uuid:project_id>', RetrieveUpdateDestroyProject.as_view()),
    path('projects/', ListCreateProject.as_view()),
    path('projects/<uuid:project_id>/users/', ListCreateProjectContributor.as_view()),
]
