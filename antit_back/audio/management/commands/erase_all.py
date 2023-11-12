# your_app/management/commands/erase_all.py
from django.core.management.base import BaseCommand
from audio.models import Audio
from transcription.models import Transcription
from annotator.models import Annotator
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Remove all instances of Transcription, Audio and Annotator models"

    def handle(self, *args, **options):
        Transcription.objects.all().delete()
        Audio.objects.all().delete()
        Annotator.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("All instances removed successfully."))
