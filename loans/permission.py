from rest_framework import permissions

class MyDeletePermission(permissions.BasePermission):
    """
    Permite apenas solicitações DELETE.
    """
    def has_permission(self, request, view):
        return request.method == 'DELETE'
