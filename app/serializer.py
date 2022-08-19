from rest_framework import serializers
from . import models

class ImageSerializer(serializers.ModelSerializer):
    """Serializes feed"""

    class Meta:
        model = models.ImageModel
        fields = ('id', 'images', 'heading', 'sub_heading', 'description')
