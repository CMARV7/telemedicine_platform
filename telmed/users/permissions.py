from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsDoctor(BasePermission):
    """
    Allows access only to doctor users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'doctor'


class IsPatient(BasePermission):
    """
    Allows access only to patient users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'patient'
