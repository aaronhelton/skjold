from django.contrib import admin
from rdflib import ConjunctiveGraph
from django.conf import settings

graph = settings.GRAPH

# Register your models here.
from .models import Namespace, AssertionStatement, LiteralStatement, QuotedStatement, TypeStatement, Resource

class LiteralsInline(admin.StackedInline):
  model = LiteralStatement

class ResourceAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {
      'fields': ['subject'],
    }),
  ]
  inlines = [ LiteralsInline ]

admin.site.register(Namespace)
admin.site.register(AssertionStatement)
admin.site.register(LiteralStatement)
admin.site.register(QuotedStatement)
admin.site.register(TypeStatement)
admin.site.register(Resource, ResourceAdmin)
