from django.conf.urls import url, include
from django.urls import path, re_path

from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('problems', views.AllProblemView)
urlpatterns = [
    url('', include(routers.urls)),
    path('problemDetail/<str:pk>/', views.ProblemDetailView.as_view(), name='problem-detail'),
    path('uploadfile/', views.UploadFileAPIView.as_view()),
    path('downloadfile/', views.filedown, name='download'),
    path('showpic/', views.showPic, name='show_picture'),
    path('judgeFileDown/', views.judgeFileDown, name='judgeFileDown'),
    path('judgeFileTime/', views.judgeFileTime, name='judgeFileTime'),
]

