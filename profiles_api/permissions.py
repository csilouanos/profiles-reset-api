from rest_framework import permissions

#Make custom permission classes
class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    #Gets call every time we call the assinged API
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        #If the request is for read only return true
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id