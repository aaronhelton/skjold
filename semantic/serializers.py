from rest_framework import serializers
from semantic.models import Resource, LiteralStatement, TypeStatement, AssertedStatement, QuotedStatement, Context, Klass, Namespace, Predicate

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    #literal_statements = serializers.HyperlinkedIdentityField(view_name='literal-detail', read_only=True)
    class Meta:
        model = Resource
        fields = ('subject',)

class LiteralSerializer(serializers.ModelSerializer):

    class Meta:
        model = LiteralStatement
        fields = ('id','subject','predicate','object','objlanguage', 'objdatatype','context')

class TypeStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeStatement
        fields = ('id','member','klass')

class AssertedStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssertedStatement
        fields = ('id','subject','predicate','object')

class QuotedStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuotedStatement
        fields = ('id','subject','predicate','object', 'objlanguage')

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Klass
        fields = ('value',)

class ContextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Context
        fields = ('value',)

class PredicateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Predicate
        fields = ('value',)

class NamespaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Namespace
        fields = ('prefix','uri')
