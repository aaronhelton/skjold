from django.db import models
from django.conf import settings
import hashlib, json
from django.core.exceptions import ValidationError
from rdflib import ConjunctiveGraph, URIRef, Literal, RDF
from rdflib_sqlalchemy.store import SQLAlchemy
from rdflib_sqlalchemy.termutils import type_to_term_combination
from rdflib_sqlalchemy.termutils import statement_to_term_combination

graph = settings.GRAPH
identifier = settings.IDENTIFIER

class Resource(models.Model):
  subject = models.URLField(primary_key=True)

  def __str__(self):
    return json.dumps(self.subject)

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

class Context(models.Model):
  value = models.TextField(primary_key=True)

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

class AssertedStatement(models.Model):
  id = models.AutoField(primary_key=True)
  subject = models.ForeignKey(Resource, to_field='subject', db_column='subject', related_name='asserted_statements')
  predicate = models.ForeignKey(Predicate, to_field='value', db_column='predicate')
  object = models.ForeignKey(Resource, to_field='subject', db_column='object', related_name='as_object')
  context = models.ForeignKey(Context, to_field='value', db_column='context')
  # termcomb here is calculated via int(statement_to_term_combination(subject, predicate, obj, context))
  termcomb = models.IntegerField(default=0)

  class Meta:
    db_table = 'kb_' + identifier + '_asserted_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.subject.subject) + " " + graph.qname(self.predicate.value) + " " + graph.qname(self.object.subject)

  #overrides
  def save(self, *args, **kwargs):
    #assumption is all three are URIRef. This might not be true.
    self.termcomb = int(statement_to_term_combination(URIRef(self.subject.subject), URIRef(self.predicate.value), URIRef(self.object.subject), graph.get_context(self.context.value)))
    super(AssertedStatement, self).save(*args, **kwargs)

class LiteralStatement(models.Model):
  id = models.AutoField(primary_key=True)
  subject = models.ForeignKey(Resource, to_field='subject', db_column='subject', related_name='literal_statements')
  predicate = models.ForeignKey(Predicate, to_field='value', db_column='predicate')
  object = models.TextField()
  context = models.ForeignKey(Context, to_field='value', db_column='context')
  # here, termcomb is built via int(statement_to_term_combination(subject, predicate, obj, context))
  termcomb = models.IntegerField(default=0)
  # pre-save validation should try to catch that only one of the following is filled in
  objlanguage = models.CharField(max_length=255, blank=True, null=True)
  objdatatype = models.CharField(max_length=255, blank=True, null=True)

  class Meta:
    db_table = 'kb_' + identifier + '_literal_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.subject.subject) + " " + graph.qname(self.predicate.value) + " " + self.object

  #overrides
  def save(self, *args, **kwargs):
    self.termcomb = int(statement_to_term_combination(URIRef(self.subject.subject), URIRef(self.predicate.value), Literal(self.object), graph.get_context(self.context.value)))
    super(LiteralStatement, self).save(*args, **kwargs)


# None of the triple sets I have worked with so far end up in the QuotedStatement model, so I am not
# making use of it in the admin. If you know what it is/does, by all means feel free to connect it up.
# I have made it ready and will maintain it to the same degree as the other *Statement models.
class QuotedStatement(models.Model):
  id = models.AutoField(primary_key=True)
  subject = models.ForeignKey(Resource, to_field='subject', db_column='subject', related_name='quoted_statements')
  predicate = models.URLField()
  object = models.TextField()
  context = models.ForeignKey(Context, to_field='value', db_column='context')
  termcomb = models.IntegerField(default=0)
  objlanguage = models.CharField(max_length=255, blank=True, null=True)
  objdatatype = models.CharField(max_length=255, blank=True, null=True)

  class Meta:
    db_table = 'kb_' + identifier + '_quoted_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.subject) + " " + graph.qname(self.predicate) + " " + self.object

  #overrides
  def save(self, *args, **kwargs):
    self.termcomb = int(statement_to_term_combination(URIRef(self.subject.subject), URIRef(self.predicate.value), Literal(self.object), graph.get_context(self.context.value)))
    super(QuotedStatement, self).save(*args, **kwargs)

class TypeStatement(models.Model):
  id = models.AutoField(primary_key=True)
  member = models.ForeignKey(Resource, to_field='subject', db_column='member', related_name='types')
  klass = models.URLField()
  context = models.ForeignKey(Context, to_field='value', db_column='context')
  # termcomb needs to be calculated via int(rdflib_sqlalchemy.termutils.type_to_term_combination(member,klass,context))
  termcomb = models.IntegerField(default=0)

  class Meta:
    db_table = 'kb_' + identifier + '_type_statements'
    managed = False

  def __str__(self):
    return graph.qname(self.member.subject) + " " + graph.qname(RDF.type) + " " + graph.qname(self.klass) + " (" + self.context.value + ")"

  #overrides
  def save(self, *args, **kwargs):
    # The only problem is that we can't know ahead of time whether our member/klass/context values are of type
    # BNode, Literal, URIRef, or Variable. Casting and testing for exceptions isn't helpful, so I'm not sure
    # what approach to take here.
    self.termcomb = int(type_to_term_combination(URIRef(self.member.subject), URIRef(self.klass), graph.get_context(self.context.value)))
    super(TypeStatement, self).save(*args, **kwargs)
