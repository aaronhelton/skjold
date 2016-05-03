SkjoLD Semantic Platform
========================

This repository aims to provide a generic web platform to serve and manage RDF data. 

It is a Django application backed by RDFLib-SQLAlchemy on a Postgres database.

Quick Start
-----------

Make sure you have a Postgres database installed and running. Create a user and database for your application. The default username:password combo is skjold:password, and the default database name is skjold. 

Clone the repository and install the requirements:

    $ pip install -r requirements.txt

Run migrations:

    $ ./manage.py migrate

Create a superuser:

    $ ./manage.py createsuperuser

Run the loadstor management command to populate your database. Make sure to supply both a path to a RDF file and the name of the graph you want to use for it:

    $ ./manage.py loadstor /path/to/rdf/data.ttl graphname

Now you can run the server and point your browser to, e.g., http://localhost:4000/admin where you can login and manage the RDF graph.

Notes
-----

The effort to harmonize Django's data models with those of RDFLib-SQLAlchemy required additions to the RDFLib-SQLAlchemy library. You'll need >= version 0.3.dev0 (clone https://github.com/RDFLib/rdflib-sqlalchemy) to make use of these additions. 

Also, I have added my own supplementary managed models (the RDFLib-SQLAlchemy models are unmanaged) that hold unique lists of, e.g., Resources, OWL Classes, Predicates, and such. For instance, the contextualized triple 

    (s,p,o,c) (ns1:Foo,rdf:type,owl:Thing,context); 

would have an entry in the Resource model for ns1:Foo, an entry in the Predicate model for rdf:type, an entry in the Klass model for owl:Thing, and an entry in the Context model for context. 

To Do
-----

These are the things I think I still need to do, but I haven't fully evaluated all of them.

1. Figure out how to import any combination of ontologies and instances without cluttering the graphs.
2. Build web-based admin for aspect CRUD, complete with roles.
3. Improve web admin forms for the triplestore, perhaps with autocompletes and more compact views.
4. Create a basic HTML (non-admin) interface for viewing graphs and browsing by rdf:type.
5. Build out non-HTML views like JSON-LD, RDF/Turtle, and RDF/XML.
6. Search.
7. SPARQL endpoint?

Contributing
------------

Contributions are welcome and encouraged. Noting the license below, all new contributors to the code base are asked to dedicate their contributions to the public domain. If you want to send a patch or enhancement for possible inclusion in the source tree, please accompany the patch with the following statement:

_The author or authors of this code dedicate any and all copyright interest in this code to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this code under copyright law._

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
