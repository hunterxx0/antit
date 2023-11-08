from django.core.exceptions import ValidationError
from audio.models import Audio
from django.db.models import (
    Model,
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)


class Transcription(Model):
    audio = ForeignKey(Audio, related_name="transcriptions", on_delete=CASCADE)
    transcription = TextField(blank=True, null=True)
    user = ForeignKey("auth.User", on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        self.validate_transcription()

    def validate_transcription(self):
        character_set = "()'aA-àÀ?â .,;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "

        last_char = ""
        capitalized = False
        for char in self.transcription:
            if char not in character_set:
                raise ValidationError(f"Invalid character in transcription: '{char}'")

            if char.isalpha():
                if char.isupper():
                    if not last_char or last_char.isspace():
                        capitalized = True
                    elif not capitalized:
                        raise ValidationError(
                            "Invalid capitalization in the transcription."
                        )
                else:
                    capitalized = False

            last_char = char

        if self.transcription[-1] in ["?", "!", "."]:
            pass
        elif self.transcription[-1] in [",", ";", ":"]:
            if self.transcription[-2] != " ":
                raise ValidationError("Ending punctuation is not followed by a space.")
        elif self.transcription[-1] != " ":
            raise ValidationError("Transcription must end with proper punctuation.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
