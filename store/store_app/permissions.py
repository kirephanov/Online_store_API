from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    A custom permission that allows only the owners to edit the object.
    '''
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Recording rights are granted only to the owner.
        return obj.owner == request.user