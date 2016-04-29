from django.db import models
from django.conf import settings
import hashlib
from rdflib import ConjunctiveGraph, URIRef, RDF
from rdflib_sqlalchemy.SQLAlchemy import SQLAlchemy

graph = settings.GRAPH
identifier = settings.IDENTIFIER

class Resource(models.Model):
  subject = models.URLField(primary_key=True)

  def __str__(self):
    return self.subject

class Klass(models.Model):
  value = models.URLField(primary_key=True)

  class Meta:
    verbose_name = 'Class'
    verbose_name_plural = 'Classes'

  def __str__(self):
    return self.value

class Predicate(models.Model):
  value = models.URLField(primary_key=True)

  def __str__(self):
    return self.value

#unmanaged models from rdflib_sqlalchemy
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
  #subject = models.URLField()
  subject = models.ForeignKey(Resource, to_field='subject', db_column='subject', related_name='as_subject')
  #predicate = models.URLField()
  predicate = models.ForeignKey(Predicate, to_field='value', db_column='predicate')
  #object = models.URLField()
  object = models.ForeignKey(Resource, to_field='subject', db_column='object', related_name='as_object')
  context = models.TextField()
  termcomb = models.IntegerField()

  class Meta:
    db_table = 'kb_' + identifier + '_asserted_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.subject.subject) + " " + graph.qname(self.predicate.value) + " " + graph.qname(self.object.subject)

class LiteralStatement(models.Model):
  #subject = models.URLField() 
  subject = models.ForeignKey(Resource, to_field='subject', db_column='subject')
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
    return graph.qname(self.subject.subject) + " " + graph.qname(self.predicate) + " " + self.object

class QuotedStatement(models.Model):
  id = models.AutoField(primary_key=True)
  #subject = models.URLField()
  subject = models.ForeignKey(Resource, to_field='subject', db_column='subject')
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
  #member = models.URLField()
  member = models.ForeignKey(Resource, to_field='subject', db_column='member')
  klass = models.URLField()
  context = models.TextField()
  termcomb = models.IntegerField()

  class Meta:
    db_table = 'kb_' + identifier + '_type_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.member.subject) + " " + graph.qname(RDF.type) + " " + graph.qname(self.klass) + " (" + self.context + ")"
