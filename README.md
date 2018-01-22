SkjoLD Semantic Platform
========================

This repository aims to provide a generic web platform to serve and manage RDF data. 

It is a Django application backed by RDFLib-SQLAlchemy on a Postgres database.

Quick Start
-----------

The repository works with Docker and can provision resources via docker-compose. This is the recommended approach, although it is possible to follow a normal Django setup process as well. To start with Docker:

Make sure Docker is installed and the Docker daemon is running. 

Clone the repository and cd into the directory you cloned to.

From here, you want to build your images, which could take a while:

    $ docker-compose build

Now you're ready to bring up the services in daemon mode:

    $ docker-compose up -d

Your application is listening on port 80 of your Docker default machine, e.g., http://192.168.99.100/

Run your migrations:

    $ docker-compose run web python manage.py migrate

Create a superuser:

    $ docker-compose run web python manage.py createsuperuser

And load your files. While the non-Docker startup will let you load from the local filesystem, in the Docker startup, you will need to specify a URL:

    $ docker-compose run web python manage.py loadstor http://path.to/some/rdf.ttl graphname

If you want to use the admin and have it look pretty, you will want to collect the static files:

    $ docker-compose run web python manage.py collectstatic --noinput

If all went well, you should be able to navigate to, e.g., http://192.168.99.100/admin and login as the superuser you made. Since there are no public endpoints, all management is done in the admin.

Notes
-----
I have added my own supplementary managed models (the RDFLib-SQLAlchemy models are unmanaged) that hold unique lists of, e.g., Resources, OWL Classes, Predicates, and such. For instance, the contextualized triple 

    (s,p,o,c) (ns1:Foo,rdf:type,owl:Thing,context); 

would have an entry in the Resource model for ns1:Foo, an entry in the Predicate model for rdf:type, an entry in the Klass model for owl:Thing, and an entry in the Context model for context. 

To Do
-----

These are the things I think I still need to do, but I haven't fully evaluated all of them.

1. Create a basic HTML (non-admin) interface for viewing graphs and browsing by rdf:type.
2. Build out non-HTML views like JSON-LD, RDF/Turtle, and RDF/XML.
3. Search.

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
