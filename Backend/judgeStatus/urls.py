# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('judgeStatus', views.JudgeStatusView)


urlpatterns = [
    url('', include(routers.urls)),
    path('judgeStatusPut/', views.JudgeStatusPutView.as_view({'post': 'create'}), name='judgeStatus-create'),
    path('judgeStatusCode/<int:pk>/', views.JudgeStatusCodeView.as_view({'get': 'retrieve'}), name='judgeStatusCode'
                                                                                                   '-retrieve'),
    # path('rejudge/', views.RejudgeAPIView.as_view()),
]
