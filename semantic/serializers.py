from rest_framework import serializers
from semantic.models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('subject',)
