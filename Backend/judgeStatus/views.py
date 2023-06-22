# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.pagination import LimitOffsetPagination
from .models import JudgeStatus
from .serializers import GetSerializer, JudgeStatusCodeSerializer, JudgeStatusSerializer
from .permission import ManagerOnly


# 普通查找试图
class JudgeStatusView(viewsets.ModelViewSet):
    queryset = JudgeStatus.objects.all().order_by('-id')
    serializer_class = GetSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, ]
    search_fields = ['username__username', 'problemID__id']
    permission_classes = [ManagerOnly, ]
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


# 加入一条判题信息
class JudgeStatusPutView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = JudgeStatus.objects.all()
    serializer_class = JudgeStatusSerializer
    permission_classes = [AllowAny, ]
    throttle_scope = "judge"
    throttle_classes = [ScopedRateThrottle, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Successfully submit your code!'}, status=status.HTTP_201_CREATED, headers=headers)


# 查看源代码的试图
class JudgeStatusCodeView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = JudgeStatus.objects.all()
    serializer_class = JudgeStatusCodeSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, ]
    search_fields = ['id']
    permission_classes = [AllowAny, ]
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]
