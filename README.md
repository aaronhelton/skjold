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

Also, I have added my own managed model (the RDFLib-SQLAlchemy models are unmanaged) that holds copies of each unique RDF resource (i.e., anything that has rdf:type) to act as an entry point for the set of inbound and outbound triples associated with it. For instance, 

    ns1:Foo a owl:Thing ; 

would have an entry in the Resource model, but it has to be copied there upon the creation of any typed thing. This is a workaround for Django's inability to have compound primary keys. 

To Do
-----

These are the things I think I still need to do, but I haven't fully evaluated all of them.

1. Add more information to the delete_confirm page to indicate that deleting a Resource will also delete the triples associated with it, which while not strictly necessary, is nevertheless indicated as a time-saving measure; otherwise users will have to hunt down all associated triples by hand.
2. Build out the Resource creation admin interface. As it stands, one must create the resource and then create each separate triple from scratch. At the very least, adding triples from a Resource admin page should populate the subject or object portion of the triple.
3. Create a basic HTML (non-admin) interface for viewing graphs and browsing by rdf:type.
4. Build out non-HTML views like JSON-LD, RDF/Turtle, and RDF/XML.
5. Search.
6. Better import tools.
7. Build out API hooks to support special-purpose applications drawn from the general-purpose platform. 
8. SPARQL endpoint?

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
