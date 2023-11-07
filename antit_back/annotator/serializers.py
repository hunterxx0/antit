from rest_framework.serializers import ModelSerializer
from .models import Audio


class AudioSerializer(ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"
