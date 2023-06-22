from django.urls import path

from django.conf.urls import url, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('users', views.UserView)

urlpatterns = [
    url('', include(routers.urls)),
    path('register/', views.UserRegisterAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('logout/', views.UserLogoutAPIView.as_view()),
    path('changeone/', views.UserChangeView.as_view()),
    path('changeall/', views.UserChangeAllView.as_view()),
]
