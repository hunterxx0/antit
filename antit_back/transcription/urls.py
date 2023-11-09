from django.urls import path
from .views import TranscriptionView

urlpatterns = [
    path(
        "<int:audio_pk>/transcriptions/",
        TranscriptionView.as_view({"get": "list", "post": "create"}),
        name="transcription-list",
    ),
    path(
        "<int:audio_pk>/transcription/update/<int:pk>/",
        TranscriptionView.as_view({"put": "update"}),
        name="transcription-detail",
    ),
]
