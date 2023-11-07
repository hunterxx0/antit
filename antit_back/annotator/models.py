from django.contrib.auth.models import User
from django.db.models import (
    Model,
    FileField,
    TextField,
    DateTimeField,
    FloatField,
    OneToOneField,
    CASCADE,
)


class Audio(Model):
    audio_file = FileField(upload_to="audio_files/")
    transcription = TextField(blank=True, null=True)
    duration = FloatField()
    created_at = DateTimeField(auto_now_add=True)


class Annotator(Model):
    user = OneToOneField(User, on_delete=CASCADE)
