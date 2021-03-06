from datetime import datetime
from rest_framework import permissions, generics
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from users.models import User
from issuetracker.models import Comment, Project, Contributor, Issue
from issuetracker.permissions import IsOwnerOfProject, IsOwner, IsContributor
from issuetracker.serializers import (ProjectSerializer,
                                      ContributorListSerializer,
                                      ContributorDetailsSerializer,
                                      IssueSerializer,
                                      CommentSerializer)


class ListCreateProject(generics.ListCreateAPIView):
    """
    This view allows you to list all available projects and create new one.

    Model: Project
    Allowed methods: GET, POST.
    """

    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        '''Get only the list of projects of the logged in user.'''
        user = self.request.user
        return Project.objects.filter(author_user_id=user)

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)


class RetrieveUpdateDestroyProject(generics.RetrieveUpdateDestroyAPIView):
    """
    This view allows you to view a project details, edit it or delete it.

    Model: Project
    Allowed methods: GET, PUT, PATCH, DELETE.
    """

    lookup_url_kwarg = 'project_id'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfProject]


class ListCreateProjectContributor(generics.ListCreateAPIView):
    """
    This view allows you to list all contributors of a project & add a new one.

    Model: Contributor (through table User<>Project)
    Allowed methods: GET, POST.
    """

    queryset = Contributor.objects.all()
    serializer_class = ContributorListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            project = get_object_or_404(Project,
                                        id=self.kwargs.get('project_id'))
            if not project.author_user_id == self.request.user:
                raise PermissionDenied({"message":
                                        "You don't have permission to access this project"})
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
    """
    This view allows you to delete a contributor from a project.

    Model: Contributor
    Allowed methods: DELETE.
    """

    serializer_class = ContributorListSerializer
    lookup_field = 'user_id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfProject]

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        user = get_object_or_404(User, id=self.kwargs.get('user_id'))
        queryset = Contributor.objects.filter(project=project, user=user)
        return queryset


class ListCreateIssue(generics.ListCreateAPIView):
    """
    This view allows you to list all issues of a project & create a new one.

    Model: Issue
    Allowed methods: GET, POST.
    """

    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsContributor]

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
    """
    This view allows you to view an issue details, edit it or delete it.

    Model: Issue
    Allowed methods: GET, PUT, PATCH, DELETE.
    """

    serializer_class = IssueSerializer
    lookup_url_kwarg = 'issue_id'
    permission_classes = [permissions.IsAuthenticated, IsOwner, IsContributor]

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        queryset = project.issue_set.filter(id=self.kwargs.get('issue_id'))
        return queryset

    def perform_update(self, serializer):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        author = self.request.user
        now = datetime.now()
        serializer.save(project_id=project, author=author, created_time=now)


class ListCreateComment(generics.ListCreateAPIView):
    """
    This view allows you to list all comments of an issue & create a new one.

    Model: Comment
    Allowed methods: GET, POST.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsContributor]

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        issue = project.issue_set.filter(id=self.kwargs.get('issue_id'))
        queryset = Comment.objects.filter(issue__in=issue)
        return queryset

    def perform_create(self, serializer):
        issue = get_object_or_404(Issue, id=self.kwargs.get('issue_id'))
        author = self.request.user
        now = datetime.now()
        serializer.save(author=author, created_time=now, issue=issue)


class RetrieveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
    """
    This view allows you to view a comment details, edit it or delete it.

    Model: Comment
    Allowed methods: GET, PUT, PATCH, DELETE.
    """

    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [permissions.IsAuthenticated, IsOwner, IsContributor]

    def get_queryset(self):
        issue = get_object_or_404(Issue, id=self.kwargs.get('issue_id'))
        queryset = issue.comment_set.filter(id=self.kwargs.get('comment_id'))
        return queryset

    def perform_update(self, serializer):
        project = get_object_or_404(Project, id=self.kwargs.get('project_id'))
        author = self.request.user
        now = datetime.now()
        serializer.save(project_id=project, author=author, created_time=now)
