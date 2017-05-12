from rest_framework import serializers
from semantic.models import Resource, LiteralStatement, TypeStatement, AssertedStatement, QuotedStatement, Context, Klass, Namespace, Predicate
from rdflib_sqlalchemy.termutils import type_to_term_combination
from rdflib_sqlalchemy.termutils import statement_to_term_combination
from rdflib import URIRef, Literal
from django.conf import settings

graph = settings.GRAPH

class LiteralSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='literal-detail')

    class Meta:
        model = LiteralStatement
        fields = ('id','url','subject','predicate','object','objlanguage', 'objdatatype','termcomb','context')

class TypeStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeStatement
        fields = ('id','member','klass','context','termcomb')

class AssertedStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssertedStatement
        fields = ('id','subject','predicate','object','context','termcomb')

class QuotedStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuotedStatement
        fields = ('id','subject','predicate','object', 'objlanguage','objdatatype','termcomb')

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Klass
        fields = ('value',)

class ContextSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='context-detail',lookup_field='value')

    class Meta:
        model = Context
        fields = ('url','value')

class PredicateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Predicate
        fields = ('value',)

class NamespaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Namespace
        fields = ('prefix','uri')

#this goes last to take advantage of the prior serializers
class ResourceSerializer(serializers.ModelSerializer):
    subject = serializers.URLField()
    literal_statements = LiteralSerializer(many=True, read_only=True)
    asserted_statements = AssertedStatementSerializer(many=True, read_only=True)
    quoted_statements = QuotedStatementSerializer(many=True, read_only=True)
    types = TypeStatementSerializer(many=True, read_only=True)
    class Meta:
        model = Resource
        fields = ('subject','literal_statements','asserted_statements','quoted_statements','types')
