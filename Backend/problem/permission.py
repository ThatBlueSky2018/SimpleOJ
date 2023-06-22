from rest_framework import permissions


class ManagerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # 'GET', 'HEAD', 'OPTIONS‘ 三种请求拥有此权限
        if request.method in permissions.SAFE_METHODS:
            return True
        _type = request.session.get('type', 1)

        # 仅管理员有写权限
        if _type == 2 or _type == 3:
            return True
        else:
            return False

