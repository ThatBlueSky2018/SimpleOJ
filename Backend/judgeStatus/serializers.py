from rest_framework import serializers
from .models import JudgeStatus


class JudgeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeStatus
        fields = '__all__'


# 不包括代码
class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeStatus
        exclude = ['code']


# 只有代码
class JudgeStatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeStatus
        fields = ['code']


