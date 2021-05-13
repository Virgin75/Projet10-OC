from rest_framework import viewsets, permissions
from rest_framework.response import Response

from issuetracker.models import Project
from issuetracker.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [permissions.IsAuthenticated]
