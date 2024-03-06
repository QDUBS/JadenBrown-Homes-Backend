from rest_framework import permissions

class PropertyManagerPermission(permissions.BasePermission):
    safe_methods = ["GET"]
    def has_object_permission(self, request, view, obj):
        method, user = request.method,request.user
        
        if method in self.safe_methods or user == "AnonymousUser":
            return True
        self.safe_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
        if user.id == obj.owner.id and method in self.safe_methods:
            return True

        return False
    
    def has_permission(self, request, view):
        method, user = request.method,request.user
        if method in self.safe_methods or user == "AnonymousUser":
            return True
        
        self.safe_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
        try:
            accont_type =request.user.user_profile.accout_type

            if accont_type == "agent" and method in self.safe_methods:
                return True
        except Exception as exec:
            return False
        
        return False