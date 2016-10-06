from semantic.models import Resource, LiteralStatement, TypeStatement, AssertedStatement
from semantic.serializers import ResourceSerializer, LiteralSerializer, TypeStatementSerializer, AssertedStatementSerializer
from rest_framework import generics
from rest_framework import permissions

class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class LiteralList(generics.ListCreateAPIView):
    queryset = LiteralStatement.objects.all()
    serializer_class = LiteralSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class LiteralDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LiteralStatement.objects.all()
    serializer_class = LiteralSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TypeStatementList(generics.ListCreateAPIView):
    queryset = TypeStatement.objects.all()
    serializer_class = TypeStatementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TypeStatementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeStatement.objects.all()
    serializer_class = TypeStatementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AssertedStatementList(generics.ListCreateAPIView):
    queryset = AssertedStatement.objects.all()
    serializer_class = AssertedStatementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AssertedStatementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssertedStatement.objects.all()
    serializer_class = AssertedStatementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
