from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
