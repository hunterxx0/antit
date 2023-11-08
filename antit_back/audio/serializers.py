from rest_framework.serializers import ModelSerializer, SerializerMethodField
from audio.models import Audio


class AudioSerializer(ModelSerializer):
    transcription_count = SerializerMethodField()

    class Meta:
        model = Audio
        fields = ["id", "audio_file", "transcription_count", "duration", "created_at"]

    def get_transcription_count(self, obj):
        return obj.transcriptions.count()
