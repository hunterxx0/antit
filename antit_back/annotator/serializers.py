from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Annotator


class AnnotatorSerializer(ModelSerializer):
    class Meta:
        model = Annotator
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
