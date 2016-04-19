from django.db import models
from django.conf import settings
import hashlib
from rdflib import ConjunctiveGraph, URIRef, RDF
from rdflib_sqlalchemy.SQLAlchemy import SQLAlchemy

graph = settings.GRAPH
identifier = settings.IDENTIFIER

class Namespace(models.Model):
  prefix = models.CharField(max_length=200, primary_key=True)
  # Because namespace URIs can end in # or /, it is unsafe to URLify them
  uri = models.CharField(max_length=200)

  class Meta:
    db_table = 'kb_' + identifier + '_namespace_binds'
    managed = False

  def __str__(self):
    return self.prefix + "|" + self.uri

class AssertionStatement(models.Model):
  id = models.AutoField(primary_key=True)
  # It is safe to force URLs here
  subject = models.URLField()
  predicate = models.URLField()
  object = models.URLField()
  context = models.TextField()
  termcomb = models.IntegerField()

  class Meta:
    db_table = 'kb_' + identifier + '_asserted_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.subject) + " " + graph.qname(self.predicate) + " " + graph.qname(self.object)

class LiteralStatement(models.Model):
  subject = models.URLField()
  predicate = models.URLField()
  object = models.TextField()
  context = models.TextField()
  termcomb = models.IntegerField()
  objlanguage = models.CharField(max_length=255)
  objdatatype = models.CharField(max_length=255)

  class Meta:
    db_table = 'kb_' + identifier + '_literal_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.subject) + " " + graph.qname(self.predicate) + " " + self.object

class QuotedStatement(models.Model):
  id = models.AutoField(primary_key=True)
  subject = models.URLField()
  predicate = models.URLField()
  object = models.TextField()
  context = models.TextField()
  termcomb = models.IntegerField()
  objlanguage = models.CharField(max_length=255)
  objdatatype = models.CharField(max_length=255)

  class Meta:
    db_table = 'kb_' + identifier + '_quoted_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.subject) + " " + graph.qname(self.predicate) + " " + self.object

class TypeStatement(models.Model):
  id = models.AutoField(primary_key=True)
  member = models.URLField()
  klass = models.URLField()
  context = models.TextField()
  termcomb = models.IntegerField()

  class Meta:
    db_table = 'kb_' + identifier + '_type_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.member) + " " + graph.qname(RDF.type) + " " + graph.qname(self.klass) + " (" + self.context + ")"

# Managed models

class Resource(models.Model):
  subject = models.TextField()
  namespace = models.ForeignKey(Namespace,blank=True,null=True)

  def __str__(self):
    if self.namespace:
      return self.namespace.uri + self.subject
    else:
      return self.subject

  def get_outbound_assertions(self):
    return AssertionStatement.objects.all().filter(subject=self.__str__)

  def get_inbound_assertions(self):
    return AssertionStatement.objects.all().filter(object=self.__str__)

  def get_outbound_literals(self):
    return LiteralStatement.objects.all().filter(subject=self.__str__)

  def triples(self):
    return list(graph.triples((self.__str__(),None,None))) + list(graph.triples((None,None,self.__str__())))

