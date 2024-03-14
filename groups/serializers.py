from rest_framework import serializers
from groups.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(label="Username", write_only=True)
    password = serializers.CharField(
        label="Password",
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
                msg = "Access denied: wrong username or password."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
        )
