from rest_framework.serializers import ModelSerializer, SerializerMethodField
from audio.models import Audio


class AudioSerializer(ModelSerializer):
    transcription_count = SerializerMethodField()
    annotated = SerializerMethodField()

    class Meta:
        model = Audio
        fields = [
            "id",
            "audio_file",
            "transcription_count",
            "annotated",
            "duration",
            "created_at",
        ]

    def get_transcription_count(self, obj):
        return obj.transcriptions.count()

    def get_annotated(self, obj):
        user_id = self.context.get("request").query_params.get("user_id", None)
        if user_id:
            return obj.transcriptions.filter(user=user_id).exists()
        return False
