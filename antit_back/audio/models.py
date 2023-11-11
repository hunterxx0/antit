from django.db.models import (
    Model,
    FileField,
    DateTimeField,
    FloatField,
)


class Audio(Model):
    audio_file = FileField(upload_to="audio_files/")
    duration = FloatField()
    created_at = DateTimeField(auto_now_add=True)
