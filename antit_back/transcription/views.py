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
        """List method to get all transcriptions for a particular audio"""
        transcriptions = Transcription.objects.filter(audio_id=audio_pk)
        serializer = TranscriptionSerializer(transcriptions, many=True)
        return Response(serializer.data)

    def create(self, request, audio_pk=None):
        """Create method to add a new transcription"""
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

    def update(self, request, pk=None, audio_pk=None):
        """Update method to modify an existing transcription"""
        try:
            transcription = Transcription.objects.get(id=pk, audio_id=audio_pk)
        except Transcription.DoesNotExist:
            return Response(
                {"failed": "Transcription not found"}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            serializer = TranscriptionSerializer(
                transcription, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"failed": e}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
