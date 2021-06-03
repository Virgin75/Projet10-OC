from rest_framework import permissions
from issuetracker.models import Project, Contributor


class IsOwnerOfProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only owner of the object are allowed to retrieve and edit it.
        if isinstance(obj, Project):
            return obj.author_user_id == request.user
        elif isinstance(obj, Contributor):
            return obj.project.author_user_id == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only owner of the object are allowed to retrieve and edit it.
        # Those wo do not own the object can read it.
        if request.method == 'GET':
            return True
        return obj.author == request.user


class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only contributors of the object are allowed to retrieve and edit it.
        project = Project.objects.get(
            id=request.parser_context['kwargs']['project_id'])
        allowed_contributors = Contributor.objects.filter(project=project)

        allowed_users = [contributor.user for contributor in allowed_contributors]

        if request.user in allowed_users:
            return True
        return False
