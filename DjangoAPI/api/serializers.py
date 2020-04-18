from rest_framework import serializers
from .models import Fuser, Face


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)

    class Meta:
        model = Fuser
        fields = ['username', 'password', 'email']


class FaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Face
        fields = ['username', 'face']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = Fuser
        fields = ['username', 'password']


class LoginWithFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = ['face']


class UserInfoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    sex = serializers.BooleanField()
    job = serializers.CharField(max_length=50)
    tel = serializers.CharField(max_length=20)

    def update(self, instance, validated_data):
        instance.age = validated_data.get('age', instance.age)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.job = validated_data.get('job', instance.job)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.email = validated_data.get('email', instance.email)
        return instance

    class Meta:
        model = Fuser
        fields = ['id', 'username', 'age', 'sex', 'job', 'tel', 'email']


# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Comment(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         return instance

