from django.core.exceptions import ValidationError
from audio.models import Audio
from django.db.models import (
    Model,
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)

VALIDATION_SET = (
    "()'aA-àÀ?â .,;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "
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
        last_char = ""
        capitalized = False
        transcrip = self.transcription
        limit = len(transcrip)
        for idx in range(0, limit):
            if transcrip[idx] not in VALIDATION_SET:
                raise ValidationError(
                    f"Invalid character in transcription: '{transcrip[idx]}'"
                )
            # TODO Change the approach
            if transcrip[idx].isalpha():
                if transcrip[idx].isupper():
                    if (
                        not last_char
                        or (
                            last_char.isspace()
                            and idx < limit
                            and transcrip[idx + 1].isupper()
                        )
                        or (
                            last_char.isupper()
                            and idx < limit
                            and transcrip[idx + 1].isalpha()
                            and transcrip[idx + 1].isupper()
                        )
                    ):
                        capitalized = True
                    elif not capitalized or (
                        last_char.isupper()
                        and idx < limit
                        and transcrip[idx + 1].islower()
                        and transcrip[idx + 1].isalpha()
                    ):
                        print(
                            f"trans={transcrip}*\nchar={transcrip[idx]}*\nlast={last_char}*"
                        )
                        raise ValidationError(
                            "Invalid capitalization in the transcription."
                        )
                else:
                    capitalized = False

            last_char = transcrip[idx]

        if transcrip[-1] in ["?", "!", "."]:
            pass
        elif transcrip[-1] in [",", ";", ":"]:
            if transcrip[-2] != " ":
                raise ValidationError("Ending punctuation is not followed by a space.")
        elif transcrip[-1] != " ":
            raise ValidationError("Transcription must end with proper punctuation.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
