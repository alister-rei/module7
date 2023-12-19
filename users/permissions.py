from rest_framework.permissions import BasePermission, SAFE_METHODS

from main.services import is_member
from users.models import UserRoles


class OwnerOrModerator(BasePermission):

    def has_object_permission(self, request, view, obj):
        if is_member(request.user):
            return True
        return obj.owner == request.user


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить PUT, PATCH или DELETE запросы только владельцу объекта
        return obj.owner == request.user


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class NotModerator(BasePermission):

    def has_permission(self, request, view):
        return not is_member(request.user)

