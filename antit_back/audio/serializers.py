from rest_framework.serializers import ModelSerializer
from audio.models import Audio, Transcription


class AudioSerializer(ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"


class TranscriptionSerializer(ModelSerializer):
    class Meta:
        model = Transcription
        fields = "__all__"
