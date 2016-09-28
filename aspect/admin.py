from django.contrib import admin
# Register your models here.
from .models import Aspect
from semantic.models import Context, Klass

class ContextInline(admin.TabularInline):
  model = Aspect.contexts.through
  extra = 0
  verbose_name = "Aspect Context"
  verbose_name_plural = "Aspect Contexts"

class ClassInline(admin.TabularInline):
  model = Aspect.classes.through
  extra = 1
  verbose_name = "Aspect Class Selection"
  verbose_name_plural = "Aspect Class Selections"

class AspectAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {
      'fields': ['name'],
    }),
  ]
  inlines = [ ContextInline, ClassInline ]

admin.site.register(Aspect,AspectAdmin)
