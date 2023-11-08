from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Transcription
from .serializers import TranscriptionSerializer
from django.core.exceptions import ValidationError


class TranscriptionView(ModelViewSet):
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer
    permission_classes = [AllowAny]

    def list(self, request, audio_pk=None):
        transcriptions = Transcription.objects.filter(audio_id=audio_pk)
        serializer = TranscriptionSerializer(transcriptions, many=True)
        return Response(serializer.data)

    def create(self, request, audio_pk=None):
        request.data["audio"] = audio_pk
        try:
            serializer = TranscriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error = {"failed": e}
            return Response(error, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
