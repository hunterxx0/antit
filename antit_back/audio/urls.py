from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import AudioView

router = DefaultRouter()
router.register(r"audio", AudioView)

urlpatterns = [
    path("api/", include(router.urls)),
]
