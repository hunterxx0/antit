from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Audio, Transcription
from .serializers import AudioSerializer, TranscriptionSerializer


class AudioViewSet(ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [AllowAny]


class TranscriptionViewSet(ModelViewSet):
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer

    def list(self, request, audio_pk=None):
        transcriptions = Transcription.objects.filter(audio_id=audio_pk)
        serializer = TranscriptionSerializer(transcriptions, many=True)
        return Response(serializer.data)

    def create(self, request, audio_pk=None):
        request.data["audio"] = audio_pk
        serializer = TranscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
