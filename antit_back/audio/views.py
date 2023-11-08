from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Audio
from .serializers import AudioSerializer


class AudioView(ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [AllowAny]
