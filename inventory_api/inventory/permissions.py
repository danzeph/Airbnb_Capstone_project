from rest_framework.permissions import BasePermission, is_authenticated


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.owner == request.user or request.user.is_staff