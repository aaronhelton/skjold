from django.core.management.base import BaseCommand
from rdflib import ConjunctiveGraph, Namespace, Literal, URIRef, RDF
from rdflib.resource import Resource
from rdflib.namespace import SKOS, NamespaceManager
from rdflib.store import NO_STORE, VALID_STORE
from rdflib.util import guess_format
from django.conf import settings
import requests
import os, json
from semantic.models import TypeStatement, Resource, Namespace, AssertionStatement, LiteralStatement, QuotedStatement, Klass, Predicate, Context

class Command(BaseCommand):
  help = "Load RDF into your local data store."

  def add_arguments(self, parser):
    parser.add_argument('file', nargs='+', type=str)
    parser.add_argument('graph', nargs='+', type=str)

  def handle(self, *args, **options):
    f = options['file'][0]
    g = options['graph'][0]

    graph = settings.GRAPH

    rdf_format = guess_format(f)

    graph.parse(source=f, format=rdf_format, publicID=g)

    graph.commit()

    # need to copy a unique set of resources to the Resource table
    for ts in TypeStatement.objects.values_list('member',flat=True):
      Resource.objects.update_or_create(subject=ts)

    # and unique class names and predicates to their own tables
    for a in AssertionStatement.objects.values_list('predicate',flat=True):
      Predicate.objects.update_or_create(value=a)

    for l in LiteralStatement.objects.values_list('predicate',flat=True):
      Predicate.objects.update_or_create(value=l)

    for q in QuotedStatement.objects.values_list('predicate',flat=True):
      Predicate.objects.update_or_create(value=q)

    for k in TypeStatement.objects.values_list('klass',flat=True):
      Klass.objects.update_or_create(value=k)

    for c in TypeStatement.objects.values_list('context',flat=True):
      Context.objects.update_or_create(value=c)

    graph.close()

