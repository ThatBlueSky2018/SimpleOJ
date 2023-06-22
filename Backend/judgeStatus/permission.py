# coding=utf-8
from rest_framework import permissions
import datetime


# 仅管理员可查看
class ManagerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        _type = request.session.get('type', 1)
        if _type == 2 or _type == 3:
            return True
        else:
            return False
