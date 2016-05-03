from django.contrib import admin
from rdflib import ConjunctiveGraph
from django.conf import settings

graph = settings.GRAPH

# Register your models here.
from .models import Namespace, AssertedStatement, LiteralStatement, QuotedStatement, TypeStatement, Resource, Klass, Predicate, Context

class TypesInline(admin.TabularInline):
  model = TypeStatement
  extra = 0

class LiteralsInline(admin.TabularInline):
  model = LiteralStatement
  extra = 0

class AsSubjectInline(admin.TabularInline):
  model = AssertedStatement
  fk_name = 'subject'
  extra = 0
  verbose_name = 'Predicate Object'
  verbose_name_plural = 'Predicate Objects'

class AsObjectInline(admin.TabularInline):
  model = AssertedStatement
  fk_name = 'object'
  extra = 0
  verbose_name = 'Subject Predicate'
  verbose_name_plural = 'Subject Predicates'

class ResourceAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {
      'fields': ['subject'],
    }),
  ]
  inlines = [ TypesInline, AsSubjectInline, AsObjectInline, LiteralsInline ]

admin.site.register(Namespace)
admin.site.register(AssertedStatement)
admin.site.register(LiteralStatement)
admin.site.register(QuotedStatement)
admin.site.register(TypeStatement)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Klass)
admin.site.register(Predicate)
admin.site.register(Context)
