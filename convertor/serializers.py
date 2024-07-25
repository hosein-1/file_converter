from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile

class MediaSerializer(serializers.Serializer):
    media = serializers.FileField()
