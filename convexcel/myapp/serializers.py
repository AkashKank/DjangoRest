from rest_framework import serializers
from .models import Profile

class ImportSerializers(serializers.Serializer):
    file = serializers.FileField()

class PaginationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"