from rest_framework.serializers import ModelSerializer
from .models import Transcription


class TranscriptionSerializer(ModelSerializer):
    class Meta:
        model = Transcription
        fields = "__all__"
