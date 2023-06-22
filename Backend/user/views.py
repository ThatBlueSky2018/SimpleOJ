from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.generics import GenericAPIView
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_203_NON_AUTHORITATIVE_INFORMATION
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import ScopedRateThrottle
from .models import User
from .serializers import UserSerializer, UserNoPasswordSerializer
from .permission import UserSafePostOnly

TOKEN_EXPIRY_HOURS = 24  # Token过期时间（小时）


# Create your views here.

# 普通的用户视图
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserNoPasswordSerializer  # 普通视图的数据传送一般不涉及密码的传送
    filter_backends = DjangoFilterBackend, filters.SearchFilter
    filter_fields = ['password', ]  # 对password进行过滤,避免密码泄露
    search_fields = ['username', ]
    permission_classes = [UserSafePostOnly, ]
    pagination_class = LimitOffsetPagination
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


# 注册用户的视图
class UserRegisterAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username__exact=username):
            return Response({"message": "The username already exists!"}, HTTP_200_OK)

        data = request.data.copy()
        data['type'] = 1
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create_user(username=username, password=password)
            token = Token.objects.create(user=user)
            return Response({'message': "Registration successful!", 'status': 200, 'token': token.key},
                            status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# 修改用户信息时的视图
# 目前只支持修改密码
# 可能需要完善修改
class UserChangeView(APIView):
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def put(self, request):
        data = request.data.copy()
        username = request.session.get('user_id', None)
        if username is not None:
            user = User.objects.get(username=username)
            user.password = data["password"]
            user.save()
            return Response({"message": "Successfully change your information"}, status=HTTP_200_OK)

        return Response({'message': "No login!"}, status=HTTP_400_BAD_REQUEST)


# 处理用户登录事件的视图
class UserLoginAPIView(APIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': '用户名或密码错误!'}, status=status.HTTP_401_UNAUTHORIZED)

        # 删除过期的Token
        Token.objects.filter(user=user, created__lte=timezone.now() - timedelta(hours=TOKEN_EXPIRY_HOURS)).delete()
        # 获取或创建Token
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message': "Login successful!", 'status': 200, 'token': token.key},
                        status=HTTP_200_OK)


# 处理用户退出登录的视图
class UserLogoutAPIView(APIView):
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def get(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        if request.session.get('user_id', None) is not None:
            del request.session['user_id']
        if request.session.get('type', None) is not None:
            del request.session['type']
        if request.session.get('rating', None) is not None:
            del request.session['rating']
        return Response({'message': 'Successfully log out!'}, HTTP_200_OK)


# 强行修改用户所有信息的视图
class UserChangeAllView(APIView):
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def put(self, request):
        # 只有超级管理员才能修改用户的所有信息
        if request.session.get('type', None) != 3:
            return Response("You don't have permission!", status=HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        username = data["username"]
        if username is not None:
            user = User.objects.get(username=username)
            if data["password"] != ".":
                user.password = data["password"]
            user.type = data["type"]
            user.save()
            return Response("Successfully change the user's information!", status=HTTP_200_OK)
        return Response("username ERROR", status=HTTP_400_BAD_REQUEST)
