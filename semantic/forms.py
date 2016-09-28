from django import forms
from django.utils import six
from djng.forms import NgDeclarativeFieldsMetaClass, NgModelFormMixin
from .models import Namespace, AssertedStatement, LiteralStatement, QuotedStatement, TypeStatement, Resource, Klass, Predicate, Context

class ResourceForm(forms.ModelForm):

  class Meta:
    model = Resource
    fields = (subject)
