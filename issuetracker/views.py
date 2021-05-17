from rest_framework import viewsets, permissions, mixins, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from issuetracker.models import Project, Contributor
from issuetracker.serializers import ProjectSerializer, ContributorSerializer


class ListCreateProject(generics.ListCreateAPIView):
    """To edit."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDestroyProject(generics.RetrieveUpdateDestroyAPIView):
    """To edit."""
    lookup_url_kwarg = 'project_id'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ListCreateProjectContributor(generics.ListCreateAPIView):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def list(self, request, *args, **kwargs):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))

        queryset = Contributor.objects.filter(project=project)
        print(queryset.values())

        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
