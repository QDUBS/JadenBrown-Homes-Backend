from rest_framework.permissions import BasePermission

class IsAgentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_profile.accout_type != "agent":
            return False
        return super().has_permission(request, view)