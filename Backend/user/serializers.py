from rest_framework import serializers
from .models import User


# 普通的序列化器,序列化所有字段
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'type']


# 序列化除密码之外的字段
class UserNoPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'type']
