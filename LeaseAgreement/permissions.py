from rest_framework import permissions

class IsAdminOrTenantReadOnly(permissions.BasePermission):
    """
    Custom permission to grant full access to admin users.
    Tenant users have read-only access.
    """

    def has_permission(self, request, view):
        # If the user is an admin, allow full access (can do crud process on lease agreement)
        if request.user.is_staff:
            return True
        
        # If the user is a tenant, allow only safe methods (read-only)
        if hasattr(request.user, 'tenant'):
            return request.method in permissions.SAFE_METHODS
        
        # Deny access by default
        return False
