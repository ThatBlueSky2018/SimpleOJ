from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import viewsets, filters
from rest_framework.views import APIView

from .models import Problem
from .serializers import AllProblemSerializer, ProblemDetailSerializer
from .permission import ManagerOnly
from django.shortcuts import HttpResponse
from django.http import FileResponse

import base64
import os


# Create your views here.


# 获取所有的题目信息
class AllProblemView(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = AllProblemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['id', 'title']
    search_fields = ['id', 'title']
    permission_classes = [ManagerOnly, ]
    pagination_class = LimitOffsetPagination
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"list": serializer.data, "status": 200})


class ProblemDetailView(APIView):
    permission_classes = [ManagerOnly, ]
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def get(self, request, pk):
        theProblem = Problem.objects.get(pk=pk)
        if not theProblem:
            return Response({'message': "Can't find the problem!", 'status': 403},
                            status=HTTP_403_FORBIDDEN)
        serializer = ProblemDetailSerializer(instance=theProblem, many=False)
        return Response(serializer.data)


# 允许管理员上传文件
class UploadFileAPIView(APIView):
    def post(self, request):
        _type = request.session.get('type', 1)
        if _type == 1:
            return Response("Admin Only", status=HTTP_403_FORBIDDEN)

        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return Response("No file uploaded!", status=HTTP_400_BAD_REQUEST)

        destination = open("./ProblemData/" +
                           myFile.name, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        return Response('upload success', HTTP_200_OK)


# FBV
# 此函数用于下载测试数据
def filedown(request):
    _type = request.session.get('type', 1)
    if _type == 1:
        return HttpResponse("Admin Only", HTTP_403_FORBIDDEN)
    name = request.GET.get('name')
    file = open('./ProblemData/' + name + '.zip', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/msword'
    response['Content-Disposition'] = 'attachment;filename=' + name + '.zip'
    return response


# 此函数用于显示图片
def showPic(request):
    name = request.GET.get('ProblemId')
    file = open('./ProblemData/' + name + '.jpg', 'rb')
    result = file.read()

    result = base64.b64encode(result)
    return HttpResponse(result, content_type='image/jpg')


def judgeFileDown(request):
    judgersecret = "lpojdatabase"
    if os.environ.get("DB_PASSWORD"):
        judgersecret = os.environ.get("DB_PASSWORD")

    password = request.GET.get('password')
    if str(password) != str(judgersecret):
        return HttpResponse("Admin Only", HTTP_403_FORBIDDEN)

    name = request.GET.get('name')

    file = open('./ProblemData/' + name + '.zip', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/msword'
    response['Content-Disposition'] = 'attachment;filename=' + name + '.zip'
    return response


def judgeFileTime(request):
    judgersecret = "lpojdatabase"
    if os.environ.get("DB_PASSWORD"):
        judgersecret = os.environ.get("DB_PASSWORD")

    password = request.GET.get('password')
    if str(password) != str(judgersecret):
        return HttpResponse("Admin Only", HTTP_403_FORBIDDEN)

    name = request.GET.get('name')
    time = os.stat("./ProblemData/" + str(name) + ".zip").st_mtime
    return HttpResponse(time, HTTP_200_OK)
