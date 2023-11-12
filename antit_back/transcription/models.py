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
    """Transcription Model"""

    audio = ForeignKey(Audio, related_name="transcriptions", on_delete=CASCADE)
    transcription = TextField(blank=True, null=True)
    user = ForeignKey("auth.User", on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        self.validate_transcription()

    def validate_transcription(self):
        """Validate the transcription"""

        def raise_validation_error(message):
            raise ValidationError(message)

        def is_valid_character(char):
            return char.isspace() or char in VALIDATION_SET

        last_char = ""
        capitalized = False
        transcrip = self.transcription
        limit = len(transcrip)
        for idx in range(0, limit):
            if not is_valid_character(transcrip[idx]):
                raise_validation_error(
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
                    ):
                        raise_validation_error(
                            "Invalid capitalization in the transcription."
                        )
                else:
                    capitalized = False

            elif transcrip[idx] in ["?", "!", "."]:
                if (
                    idx + 1 < limit
                    and not transcrip[idx + 1].isspace()
                    or idx + 2 < limit
                    and transcrip[idx + 2].islower()
                ):
                    raise_validation_error(
                        f"'{transcrip[idx]}' should be followed by one space and an uppercase character."
                    )

            last_char = transcrip[idx]

        if transcrip[-1] in ["?", "!", "."]:
            pass
        elif transcrip[-1] in [",", ";", ":"]:
            if transcrip[-2] != " ":
                raise_validation_error("Ending punctuation is not followed by a space.")
        elif transcrip[-1] != " ":
            raise_validation_error("Transcription must end with proper punctuation.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
