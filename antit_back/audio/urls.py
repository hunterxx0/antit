from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioViewSet, TranscriptionViewSet

router = DefaultRouter()
router.register(r"audio", AudioViewSet)

transcription_router = DefaultRouter()
transcription_router.register(
    r"transcriptions", TranscriptionViewSet, basename="audio-transcriptions"
)

urlpatterns = [
    path("", include(router.urls)),
    path("/<int:audio_pk>/", include(transcription_router.urls)),
]
