from rest_framework import permissions


# 所有人用户都有读权限，仅不修改敏感信息或管理员拥有写权限
class UserSafePostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # 'GET', 'HEAD', 'OPTIONS‘ 三种请求拥有此权限
        if request.method in permissions.SAFE_METHODS:
            return True

        # 对于超级管理员,拥有写权限
        if request.session.get('type', 1) == 3:
            return True

        if request.method == "POST":
            _type = request.data.get('type', -1)
            if _type != -1:
                return False
            else:
                return True

        username = request.data.get('username')
        userid = request.session.get('user_id', None)
        if userid == username:
            return True
        else:
            return False
