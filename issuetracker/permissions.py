from rest_framework import permissions, status
from issuetracker.models import Project, Contributor
from rest_framework.exceptions import APIException


class CustomForbidden(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Page Not Found.'


class IsOwnerOfProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only owner of the object are allowed to retrieve and edit it.
        if isinstance(obj, Project):
            if obj.author_user_id == request.user:
                return True
            raise CustomForbidden
        elif isinstance(obj, Contributor):
            if obj.project.author_user_id == request.user:
                return True
            raise CustomForbidden


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only owner of the object are allowed to retrieve and edit it.
        # Those wo do not own the object can read it.
        if request.method == 'GET':
            return True
        if obj.author == request.user:
            return True
        raise CustomForbidden


class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only contributors of the object are allowed to retrieve and edit it.
        project = Project.objects.get(
            id=request.parser_context['kwargs']['project_id'])
        allowed_contributors = Contributor.objects.filter(project=project)

        allowed_users = [contributor.user for contributor in allowed_contributors]

        if request.user in allowed_users:
            return True
        raise CustomForbidden
