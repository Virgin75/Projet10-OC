from datetime import datetime

from rest_framework import viewsets, permissions, mixins, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from issuetracker.models import Project, Contributor, Issue
from issuetracker.serializers import ProjectSerializer, ContributorListSerializer, ContributorDetailsSerializer, IssueListSerializer
from users.models import User


class ListCreateProject(generics.ListCreateAPIView):
    """To edit."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDestroyProject(generics.RetrieveUpdateDestroyAPIView):
    """To edit."""
    lookup_url_kwarg = 'project_id'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ListCreateProjectContributor(generics.ListCreateAPIView):

    queryset = Contributor.objects.all()
    serializer_class = ContributorListSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        if self.request.method == 'GET':
            project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
            return super().get_queryset().filter(project=project)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContributorListSerializer
        if self.request.method == 'POST':
            return ContributorDetailsSerializer

    def perform_create(self, serializer):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        serializer.save(project=project)


class DestroyContributor(generics.DestroyAPIView):

    serializer_class = ContributorListSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        user = get_object_or_404(User, id=self.kwargs.get('user_id'))
        queryset = Contributor.objects.filter(project=project, user=user)
        return queryset


class ListCreateIssue(generics.ListCreateAPIView):

    serializer_class = IssueListSerializer

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        queryset = Issue.objects.filter(project_id=project)
        return queryset

    def perform_create(self, serializer):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        author = self.request.user
        now = datetime.now()
        serializer.save(project_id=project, author=author, created_time=now)


class UpdateDestroyIssue(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = IssueListSerializer
    lookup_field = 'id'

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        queryset = project.issue_set.filter(id=self.kwargs.get('id'))
        return queryset

    def perform_update(self, serializer):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        author = self.request.user
        now = datetime.now()
        serializer.save(project_id=project, author=author, created_time=now)
