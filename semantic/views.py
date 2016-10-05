from semantic.models import Resource
from semantic.serializers import ResourceSerializer
from rest_framework import generics

class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
