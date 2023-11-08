from django.contrib.auth.models import User

from django.db.models import (
    Model,
    FileField,
    TextField,
    DateTimeField,
    FloatField,
    ForeignKey,
    CASCADE,
)


class Audio(Model):
    audio_file = FileField(upload_to="audio_files/")
    duration = FloatField()
    created_at = DateTimeField(auto_now_add=True)


class Transcription(Model):
    audio = ForeignKey(Audio, related_name="transcriptions", on_delete=CASCADE)
    transcription = TextField(blank=True, null=True)
    user = ForeignKey("auth.User", on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
