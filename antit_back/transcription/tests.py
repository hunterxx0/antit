from django.test import TestCase
from django.core.exceptions import ValidationError
from audio.models import Audio
from transcription.models import Transcription
from django.contrib.auth.models import User


class TranscriptionModelTest(TestCase):
    def setUp(self):
        """Prep an Audio instance for testing"""
        self.audio = Audio.objects.create(audio_file="test_audio.mp3", duration=0.5)
        self.user = User.objects.create()

    def test_valid_transcription_0(self):
        """Test a valid transcription"""
        transcription = Transcription(
            audio=self.audio, transcription="Valid.", user_id=self.user.id
        )
        transcription.full_clean()

    def test_valid_transcription_1(self):
        """Test a valid transcription"""
        transcription = Transcription(
            audio=self.audio, transcription="Valid KAP.", user_id=self.user.id
        )
        transcription.full_clean()

    def test_invalid_character(self):
        """Test an invalid character in the transcription"""
        with self.assertRaises(ValidationError) as context:
            transcription = Transcription(
                audio=self.audio,
                transcription="Invalid@transcription",
                user_id=self.user.id,
            )
            transcription.full_clean()
        self.assertIn("Invalid character in transcription", str(context.exception))

    def test_invalid_capitalization_1(self):
        """Test invalid capitalization in the transcription"""
        with self.assertRaises(ValidationError) as context:
            transcription = Transcription(
                audio=self.audio,
                transcription="Invalid Kapitalization.",
                user_id=self.user.id,
            )
            transcription.full_clean()
        self.assertIn(
            "Invalid capitalization in the transcription.", str(context.exception)
        )

    def test_invalid_capitalization_2(self):
        """Test invalid capitalization in the transcription"""
        with self.assertRaises(ValidationError) as context:
            transcription = Transcription(
                audio=self.audio,
                transcription="Invalid KAPItalization.",
                user_id=self.user.id,
            )
            transcription.full_clean()
        self.assertIn(
            "Invalid capitalization in the transcription.", str(context.exception)
        )

    def test_invalid_capitalization_3(self):
        """Test invalid capitalization in the transcription"""
        with self.assertRaises(ValidationError) as context:
            transcription = Transcription(
                audio=self.audio,
                transcription="Invalid K.",
                user_id=self.user.id,
            )
            transcription.full_clean()
        self.assertIn(
            "Invalid capitalization in the transcription.", str(context.exception)
        )

    def test_invalid_ending_punctuation(self):
        """Test invalid ending punctuation in the transcription"""
        with self.assertRaises(ValidationError) as context:
            transcription = Transcription(
                audio=self.audio, transcription="Invalid ending", user_id=self.user.id
            )
            transcription.full_clean()
        self.assertIn(
            "Transcription must end with proper punctuation", str(context.exception)
        )

        with self.assertRaises(ValidationError) as context:
            transcription = Transcription(
                audio=self.audio, transcription="Invalid ending;", user_id=self.user.id
            )
            transcription.full_clean()
        self.assertIn(
            "Ending punctuation is not followed by a space", str(context.exception)
        )
