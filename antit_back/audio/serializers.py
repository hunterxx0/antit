from rest_framework.serializers import ModelSerializer
from audio.models import Audio


class AudioSerializer(ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"
