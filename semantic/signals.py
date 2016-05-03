from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from rdflib_sqlalchemy.SQLAlchemy import SQLAlchemy
from rdflib import ConjunctiveGraph, URIRef
from semantic.models import Namespace, AssertedStatement, LiteralStatement, QuotedStatement, TypeStatement, Resource
import sys

graph = settings.GRAPH

# When something is deleted from the Resource table, we want to delete all of its associated inbound and outbound triples
@receiver(pre_delete, sender=Resource)
def model_pre_change(sender, **kwargs):
  res = kwargs['instance'].__str__()
  for t in graph.triples((res,None,None)):
    graph.remove(t)

  for t in graph.triples((None,None,res)):
    graph.remove(t)

# create or update Resource table if a new subject is entered into one of our non-namespace tables
@receiver(pre_save, sender=TypeStatement)
def model_pre_change(sender, **kwargs):
  target_subject = kwargs['instance'].member
  Resource.objects.update_or_create(subject=target_subject)
