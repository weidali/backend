from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
