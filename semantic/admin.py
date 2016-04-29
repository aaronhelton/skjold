from django.contrib import admin
from rdflib import ConjunctiveGraph
from django.conf import settings

graph = settings.GRAPH

# Register your models here.
from .models import Namespace, AssertionStatement, LiteralStatement, QuotedStatement, TypeStatement, Resource, Klass, Predicate

class LiteralsInline(admin.StackedInline):
  model = LiteralStatement
  extra = 0

class AsSubjectInline(admin.TabularInline):
  model = AssertionStatement
  fk_name = 'subject'
  extra = 0

class AsObjectInline(admin.TabularInline):
  model = AssertionStatement
  fk_name = 'object'
  extra = 0

class ResourceAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {
      'fields': ['subject'],
    }),
  ]
  inlines = [ AsSubjectInline, AsObjectInline, LiteralsInline ]

admin.site.register(Namespace)
admin.site.register(AssertionStatement)
admin.site.register(LiteralStatement)
admin.site.register(QuotedStatement)
admin.site.register(TypeStatement)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Klass)
admin.site.register(Predicate)
