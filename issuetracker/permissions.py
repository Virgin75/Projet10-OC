from rest_framework import permissions
from issuetracker.models import Project, Contributor


class IsOwnerOfProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only owner of the object are allowed to retrieve and edit it.
        if isinstance(obj, Project):
            print(1)
            return obj.author_user_id == request.user
        elif isinstance(obj, Contributor):
            print(2)
            return obj.project.author_user_id == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only owner of the object are allowed to retrieve and edit it.
        # Those wo do not own the object can read it.
        if request.method == 'GET':
            return True
        return obj.author == request.user
