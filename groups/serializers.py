from rest_framework import serializers
from models import * 


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')


class StreamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stream
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')
        
