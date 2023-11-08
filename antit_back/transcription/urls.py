from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TranscriptionView

transcription_router = DefaultRouter()
transcription_router.register(r"transcription", TranscriptionView)

urlpatterns = [
    path("", include(transcription_router.urls)),
    path("<int:audio_pk>/transcribe/", include(transcription_router.urls)),
]
