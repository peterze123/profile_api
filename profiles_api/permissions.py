from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow the user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if a user has permission to edit their profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to edit their preference"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to update their status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_info.id == request.user.id