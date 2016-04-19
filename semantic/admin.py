from django.contrib import admin
from rdflib import ConjunctiveGraph

# Register your models here.
from .models import Namespace, AssertionStatement, LiteralStatement, QuotedStatement, TypeStatement, Resource

class ResourceAdmin(admin.ModelAdmin):
  readonly_fields = ('triples','literals','predicate_objects','subject_predicates')
  fieldsets = [
    (None, {
      'fields': ['namespace','subject', 'triples'],
    }),
  ]

  def triples(self, obj):
    return_html = '<ul>'
    for t in obj.triples():
      return_html = return_html + '<li>%s</li>' % str(t)

    return_html = return_html + '</ul>'
    return return_html

  def literals(self, obj):
    return_html = '<ul>'
    for l in obj.get_outbound_literals():
      return_html = return_html + '<li><a href="/admin/semantic/literalstatement/%s">%s</a></li>' % (str(l.id),l.__str__())

    return_html = return_html + '</ul>'
    return return_html

  def predicate_objects(self, obj):
    return_html = '<ul>'
    for l in obj.get_outbound_assertions():
      return_html = return_html + '<li><a href="/admin/semantic/assertionstatement/%s">%s</a></li>' % (str(l.id),l.__str__())

    return_html = return_html + '</ul>'
    return return_html

  def subject_predicates(self, obj):
    return_html = '<ul>'
    for l in obj.get_inbound_assertions():
      return_html = return_html + '<li><a href="/admin/semantic/assertionstatement/%s">%s</a></li>' % (str(l.id),l.__str__())

    return_html = return_html + '</ul>'
    return return_html

  triples.allow_tags = True
  literals.allow_tags = True
  predicate_objects.allow_tags = True
  subject_predicates.allow_tags = True

admin.site.register(Namespace)
admin.site.register(AssertionStatement)
admin.site.register(LiteralStatement)
admin.site.register(QuotedStatement)
admin.site.register(TypeStatement)
admin.site.register(Resource, ResourceAdmin)
