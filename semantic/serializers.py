from rest_framework import serializers
from semantic.models import Resource, LiteralStatement, TypeStatement, AssertedStatement

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    #literal_statements = serializers.HyperlinkedIdentityField(view_name='literal-detail', read_only=True)
    class Meta:
        model = Resource
        fields = ('subject',)

class LiteralSerializer(serializers.ModelSerializer):

    class Meta:
        model = LiteralStatement
        fields = ('id','subject','predicate','object','objlanguage')

class TypeStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeStatement
        fields = ('id','member','klass')

class AssertedStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssertedStatement
        fields = ('id','subject','predicate','object')
