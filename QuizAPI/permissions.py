from rest_framework.permissions import BasePermission



# class IsCorrectToken(BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.headers.get('AccessToken', None) == ACCESS_TOKEN)
