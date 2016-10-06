from semantic.models import Resource,LiteralStatement,TypeStatement,AssertedStatement,QuotedStatement,Klass,Predicate,Namespace,Context
from semantic.serializers import ResourceSerializer,LiteralSerializer,TypeStatementSerializer,AssertedStatementSerializer,QuotedStatementSerializer,ClassSerializer,PredicateSerializer,NamespaceSerializer,ContextSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'resources': reverse('resource-list', request=request, format=format),
        'literals': reverse('literal-list', request=request, format=format),
        'assertions': reverse('assertion-list', request=request, format=format),
        'types': reverse('type-list', request=request, format=format),
        'contexts': reverse('context-list', request=request, format=format),
        'namespaces': reverse('namespace-list', request=request, format=format),
        'predicates': reverse('predicate-list', request=request, format=format),
        'classes': reverse('class-list', request=request, format=format),
        'quotes': reverse('quote-list', request=request, format=format),
    })

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

class QuotedStatementList(generics.ListCreateAPIView):
    queryset = QuotedStatement.objects.all()
    serializer_class = QuotedStatementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class QuotedStatementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuotedStatement.objects.all()
    serializer_class = QuotedStatementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ClassList(generics.ListCreateAPIView):
    queryset = Klass.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klass.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ContextList(generics.ListCreateAPIView):
    queryset = Context.objects.all()
    serializer_class = ContextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ContextDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Context.objects.all()
    serializer_class = ContextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PredicateList(generics.ListCreateAPIView):
    queryset = Predicate.objects.all()
    serializer_class = PredicateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PredicateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Predicate.objects.all()
    serializer_class = PredicateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NamespaceList(generics.ListCreateAPIView):
    queryset = Namespace.objects.all()
    serializer_class = NamespaceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NamespaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Namespace.objects.all()
    serializer_class = NamespaceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
