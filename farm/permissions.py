from rest_framework.permissions import IsAdminUser, IsAuthenticated



class IsAuthenticatedOrEmailVisitorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and get_session_visitor_email(request):
            return True
        return IsAuthenticated().has_permission(request, view)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return IsAdminUser().has_permission(request, view)


class IsAdminOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return IsAdminUser().has_permission(request, view)