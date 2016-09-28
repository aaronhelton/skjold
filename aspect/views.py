from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rdflib import ConjunctiveGraph, URIRef, Literal, RDF, Namespace
from rdflib.namespace import SKOS, NamespaceManager

from .models import Aspect
from semantic.models import Resource

graph = settings.GRAPH
unms = Namespace('http://ontologies.un.org/undoc#')
graph.bind('unms',unms)

all_ns = [n for n in graph.namespaces()]

# Create your views here.
def index(request):
  
  return render(request, 'aspect/index.html', {'results': 'foo'})

def aspect(request, name):
  # List out members of the Aspect Class Selection (models.Aspect.classes)
  aspect = get_object_or_404(Aspect, name=name)
  # from here we can use our triplestore
  aspect_class_members = []
  for c in aspect.classes.all():
    members = graph.subjects(predicate=RDF.type,object=URIRef(c.value))
    for m in members:
      aspect_class_members.append({'term':graph.qname(m), 'pref_label':graph.preferredLabel(subject=m, lang='en')[0][1]})

  sorted_results = sorted(aspect_class_members, key=lambda tup: tup['pref_label'])

  return render(request, 'aspect/aspect.html', {'aspect_class_members': aspect_class_members})

def term(request,name,namespace,id):
  output = []
  object_id = [v[1] for i, v in enumerate(all_ns) if v[0] == 'unms'][0].__str__() + id
  for i in graph.predicate_objects(subject=URIRef(object_id)):
    output.append(i)

  return render(request, 'aspect/term.html', {'output': output, 'namespace': namespace, 'id': id})
