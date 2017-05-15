from django.core.management.base import BaseCommand
from rdflib import ConjunctiveGraph, Namespace, Literal, URIRef, RDF
from rdflib.resource import Resource
from rdflib.namespace import SKOS, NamespaceManager
from rdflib.store import NO_STORE, VALID_STORE
from rdflib.util import guess_format
from django.conf import settings
import requests
import os, json
from semantic.models import TypeStatement, Resource, Namespace, AssertedStatement, LiteralStatement, QuotedStatement, Klass, Predicate, Context

class Command(BaseCommand):
  help = "Delete the triple store"

  #def add_arguments(self, parser):
  #  parser.add_argument('file', nargs='+', type=str)
  #  parser.add_argument('graph', nargs='+', type=str)

  def handle(self, *args, **options):
    # Our signals should be able to handle the removal of triples asserted for these objects...
    Resource.objects.all().delete()


