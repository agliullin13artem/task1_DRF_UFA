from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from groups.models import Stream, Course
from groups.serializers import (
    LoginSerializer,
    StreamSerializer,
    CourseSerializer,
    UserSerializer,
)
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth import login
from django.contrib.auth import get_user_model


class StreamAPIList(ListAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer


class StreamAPICreate(CreateAPIView):
    queryset = Stream.objects.all()

    serializer_class = StreamSerializer


class CourseAPIList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class ChooseCourse(APIView):
#   def get(self, request,):
#     course = Course.objects.all()
#     serializer = CourseSerializer(course, many=True)
#     return Response(serializer.data)
#   def post(self, request,):
#     serializer = CourseSerializer(data = self.request.data, many=True)
#     serializer.is_valid()
#     sort_students(request)
#     course = Course.objects.all()
#     print(course)
#     return Response(status= status.HTTP_202_ACCEPTED, data=serializer.data)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [permissions.AllowAny]  
    serializer_class = UserSerializer
