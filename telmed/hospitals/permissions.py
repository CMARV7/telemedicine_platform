from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit or delete records.
    """
    def has_permission(self, request, view):
        # Safe methods like GET, HEAD, and OPTIONS are allowed for all users.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Only admin users can modify records.
        return request.user and request.user.is_staff
