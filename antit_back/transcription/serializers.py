from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Transcription


class TranscriptionSerializer(ModelSerializer):
    user_name = SerializerMethodField()

    class Meta:
        model = Transcription
        fields = ["id", "audio", "transcription", "user", "user_name", "created_at"]

    def get_user_name(self, obj):
        return obj.user.username.capitalize()
