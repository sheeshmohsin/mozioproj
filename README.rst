========================
Interacting With The API
========================

Api-Wide
--------

We'll start at the highest level::

    curl http://localhost:8000/api/v1/?format=json

You'll get back something like::

	{
	    "provider": {
	        "list_endpoint": "/api/v1/provider/",
	        "schema": "/api/v1/provider/schema/"
	    },
	    "service_areas": {
	        "list_endpoint": "/api/v1/service_areas/",
	        "schema": "/api/v1/service_areas/schema/"
	    }
	}

To demonstrate another format, you could run the following to get the XML
variant of the same information::

    curl -H "Accept: application/xml" http://localhost:8000/api/v1/

To which you'd receive::

	<?xml version="1.0" encoding="UTF-8"?>
	<response>
	    <provider type="hash">
	        <list_endpoint>/api/v1/provider/</list_endpoint>
	        <schema>/api/v1/provider/schema/</schema>
	    </provider>
	    <service_areas type="hash">
	        <list_endpoint>/api/v1/service_areas/</list_endpoint>
	        <schema>/api/v1/service_areas/schema/</schema>
	    </service_areas>
	</response>

We'll stick to JSON for the rest of this document, but using XML should be OK
to do at any time.

It's also possible to get all schemas (`Inspecting The Resource's Schema`_) in a single request::

    curl http://localhost:8000/api/v1/?fullschema=true

You'll get back something like::

	{
	    "provider": {
	        "list_endpoint": "/api/v1/provider/",
	        "schema": {
	            "allowed_detail_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "allowed_list_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "default_format": "application/json",
	            "default_limit": 20,
	            "fields": {
	                "currency": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "currency"
	                },
	                "email": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "email"
	                },
	                "id": {
	                    "blank": false,
	                    "default": "0a11bbfd-b3fa-4992-8e41-6a2e33060475",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": true,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": true,
	                    "verbose_name": "id"
	                },
	                "language": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "language"
	                },
	                "name": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "name"
	                },
	                "phone_number": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "phone number"
	                },
	                "resource_uri": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": true,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "resource uri"
	                }
	            }
	        }
	    },
	    "service_areas": {
	        "list_endpoint": "/api/v1/service_areas/",
	        "schema": {
	            "allowed_detail_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "allowed_list_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "default_format": "application/json",
	            "default_limit": 20,
	            "fields": {
	                "geom": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Geometry data.",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "geometry",
	                    "unique": false,
	                    "verbose_name": "geom"
	                },
	                "name": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "name"
	                },
	                "price": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Fixed precision numeric data. Ex: 26.73",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "decimal",
	                    "unique": false,
	                    "verbose_name": "price"
	                },
	                "provider": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "related_schema": "/api/v1/provider/schema/",
	                    "related_type": "to_one",
	                    "type": "related",
	                    "unique": false,
	                    "verbose_name": "provider"
	                },
	                "resource_uri": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": true,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "resource uri"
	                }
	            },
	            "filtering": {
	                "geom": 1
	            }
	        }
	    }
	}


Inspecting The Resource's Schema
--------------------------------

Since the api-wide view gave us a ``schema`` URL, let's inspect that next.
We'll use the ``provider`` resource. Again, a simple GET request by curl::

    curl http://localhost:8000/api/v1/provider/schema/

This time, we get back a lot more data::

	{
	    "allowed_detail_http_methods": [
	        "get",
	        "post",
	        "put",
	        "delete",
	        "patch"
	    ],
	    "allowed_list_http_methods": [
	        "get",
	        "post",
	        "put",
	        "delete",
	        "patch"
	    ],
	    "default_format": "application/json",
	    "default_limit": 20,
	    "fields": {
	        "currency": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": false,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "currency"
	        },
	        "email": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": false,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "email"
	        },
	        "id": {
	            "blank": false,
	            "default": "7e933da9-be06-4655-ad86-420d1424cccd",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": true,
	            "readonly": false,
	            "type": "string",
	            "unique": true,
	            "verbose_name": "id"
	        },
	        "language": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": false,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "language"
	        },
	        "name": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": false,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "name"
	        },
	        "phone_number": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": false,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "phone number"
	        },
	        "resource_uri": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": true,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "resource uri"
	        }
	    }
	}

This lists out the ``default_format`` this resource responds with, the
``fields`` on the resource & the ``filtering`` options available. This
information can be used to prepare the other aspects of the code for the
data it can obtain & ways to filter the resources.


Getting A Collection Of Resources
---------------------------------

Let's get down to fetching live data. From the api-wide view, we'll hit
the ``list_endpoint`` for ``provider``::

    curl http://localhost:8000/api/v1/provider/

We get back data that looks like::

	{
	    "meta": {
	        "limit": 20,
	        "next": null,
	        "offset": 0,
	        "previous": null,
	        "total_count": 4
	    },
	    "objects": [
	        {
	            "currency": "USD",
	            "email": "someone@gmail.com",
	            "id": "e5c5783b-0233-40aa-951a-aa44b804715f",
	            "language": "en",
	            "name": "sheesh",
	            "phone_number": "234333333534",
	            "resource_uri": "/api/v1/provider/e5c5783b-0233-40aa-951a-aa44b804715f/"
	        },
	        {
	            "currency": "USD",
	            "email": "mohsin@gmail.com",
	            "id": "cadbc0b7-5282-4ade-9d09-42dc97555873",
	            "language": "hi",
	            "name": "mohsin",
	            "phone_number": "8906406104",
	            "resource_uri": "/api/v1/provider/cadbc0b7-5282-4ade-9d09-42dc97555873/"
	        },
	        {
	            "currency": "US",
	            "email": "sodfas@gmail.com",
	            "id": "06981ee8-97b0-4560-972e-d50f11b4c5d3",
	            "language": "en",
	            "name": "fdsajkl",
	            "phone_number": "3453465345",
	            "resource_uri": "/api/v1/provider/06981ee8-97b0-4560-972e-d50f11b4c5d3/"
	        },
	        {
	            "currency": "US",
	            "email": "soejke@gmail.com",
	            "id": "893cd70a-552c-4640-aae7-89ee89765ce0",
	            "language": "en",
	            "name": "sdofd",
	            "phone_number": "34534445",
	            "resource_uri": "/api/v1/provider/893cd70a-552c-4640-aae7-89ee89765ce0/"
	        }
	    ]
	}

Some things to note:

  * By default, you get a paginated set of objects (20 per page is the default).
  * In the ``meta``, you get a ``previous`` & ``next``. If available, these are
    URIs to the previous & next pages.
  * You get a list of resources/objects under the ``objects`` key.
  * Each resources/object has a ``resource_uri`` field that points to the
    detail view for that object.
  * The foreign key to ``User`` is represented as a URI by default. If you're
    looking for the full ``UserResource`` to be embedded in this view, you'll
    need to add ``full=True`` to the ``fields.ToOneField``.

If you want to skip paginating, simply run::

    curl http://localhost:8000/api/v1/provider/?limit=0

Be warned this will return all objects, so it may be a CPU/IO-heavy operation
on large datasets.

Getting A Detail Resource
-------------------------

Since each resource/object in the list view had a ``resource_uri``, let's
explore what's there::

    curl http://localhost:8000/api/v1/provider/893cd70a-552c-4640-aae7-89ee89765ce0/

We get back a similar set of data that we received from the list view::

	{
	    "currency": "US",
	    "email": "mahvish@gmail.com",
	    "id": "893cd70a-552c-4640-aae7-89ee89765ce0",
	    "language": "en",
	    "name": "mahvish",
	    "phone_number": "9939610876",
	    "resource_uri": "/api/v1/provider/893cd70a-552c-4640-aae7-89ee89765ce0/"
	}

Selecting A Subset Of Resources
-------------------------------

Sometimes you may want back more than one record, but not an entire list view
nor do you want to do multiple requests. This API includes a "set" view, which
lets you cherry-pick the objects you want. For example, if we just want the
first & third ``provider`` resources, we'd run::

    curl "http://localhost:8000/api/v1/provider/set/1;3/"

.. note::

  Quotes are needed in this case because of the semicolon delimiter between
  primary keys. Without the quotes, bash tries to split it into two statements.
  No extraordinary quoting will be necessary in your application (unless your
  API client is written in bash :D).

And we get back just those two objects::

	{
	    "objects": [
	        {
	            "currency": "USD",
	            "email": "mohsin@gmail.com",
	            "id": "cadbc0b7-5282-4ade-9d09-42dc97555873",
	            "language": "hi",
	            "name": "mohsin",
	            "phone_number": "8743297932",
	            "resource_uri": "/api/v1/provider/cadbc0b7-5282-4ade-9d09-42dc97555873/"
	        },
	        {
	            "currency": "US",
	            "email": "ksjfdsdflk@gmail.com",
	            "id": "893cd70a-552c-4640-aae7-89ee89765ce0",
	            "language": "en",
	            "name": "lkjfds",
	            "phone_number": "34552634",
	            "resource_uri": "/api/v1/provider/893cd70a-552c-4640-aae7-89ee89765ce0/"
	        }
	    ]
	}

Note that, like the list view, you get back a list of ``objects``. Unlike the
list view, there is **NO** pagination applied to these objects. You asked for
them, you're going to get them all.

Creating A New Resource (POST)
------------------------------

Let's add a new provider. To create new data, we'll switch from ``GET`` requests
to the familiar ``POST`` request.

.. note::

    API encourages "round-trippable" data, which means the data you
    can GET should be able to be POST/PUT'd back to recreate the same
    object.

    If you're ever in question about what you should send, do a GET on
    another object & see what API thinks it should look like.

To create new resources/objects, you will ``POST`` to the list endpoint of
a resource. Trying to ``POST`` to a detail endpoint has a different meaning in
the REST mindset (meaning to add a resource as a child of a resource of the
same type).

As with all API requests, the headers we request are important. Since
we've been using primarily JSON throughout, let's send a new provider in JSON
format::

    curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"name":"fsfdsfdss", "email":"fdsfsd@gmail.com", "phone_number": "435326536", "language": "en", "currency": "US"}' http://127.0.0.1:8080/api/v1/provider/

The ``Content-Type`` header here informs API that we're sending it JSON.
We send the data as a JSON-serialized body (**NOT** as form-data in the form of
URL parameters). What we get back is the following response::

    HTTP/1.0 201 Created
	Date: Tue, 07 Jun 2016 10:27:11 GMT
	Server: WSGIServer/0.1 Python/2.7.6
	Vary: Accept
	X-Frame-Options: SAMEORIGIN
	Content-Type: application/json
	Location: /api/v1/provider/884c0999-0f23-4670-bea6-eb1e58c2e9cd/

	{"currency": "US", "email": "fdsfsd@gmail.com", "id": "884c0999-0f23-4670-bea6-eb1e58c2e9cd", "language": "en", "name": "fsfdsfdss", "phone_number": "435326536", "resource_uri": "/api/v1/provider/884c0999-0f23-4670-bea6-eb1e58c2e9cd/"}

You'll also note that we get a correct HTTP status code back (201) & a
``Location`` header, which gives us the URI to our newly created resource.

Passing ``--dump-header -`` is important, because it gives you all the headers
as well as the status code. When things go wrong, this will be useful
information to help with debugging.


Updating An Existing Resource (PUT)
-----------------------------------

You might have noticed that we made some typos when we submitted the POST
request. We can fix this using a ``PUT`` request to the detail endpoint (modify
this instance of a resource).::

    curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"name":"dsds", "email":"dsfoiaj@gmail.com", "phone_number": "4353265362", "language": "hi", "currency": "US"}' http://127.0.0.1:8080/api/v1/provider/884c0999-0f23-4670-bea6-eb1e58c2e9cd/

After fixing up the ``body``, we get back::

    HTTP/1.0 204 NO CONTENT
    Date: Fri, 20 May 2011 07:13:21 GMT
    Server: WSGIServer/0.1 Python/2.7
    Content-Length: 0
    Content-Type: text/html; charset=utf-8

We get a 204 status code, meaning our update was successful. We don't get
a ``Location`` header back because we did the ``PUT`` on a detail URL, which
presumably did not change.

.. note::

    A ``PUT`` request requires that the entire resource representation be enclosed. Missing fields may cause errors, or be filled in by default values.

Partially Updating An Existing Resource (PATCH)
-----------------------------------------------

In some cases, you may not want to send the entire resource when updating. To update just a subset of the fields, we can send a ``PATCH`` request to the detail endpoint.::

    curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"name":"dsdfsds"}' http://127.0.0.1:8080/api/v1/provider/884c0999-0f23-4670-bea6-eb1e58c2e9cd/


To which we should get back::

    HTTP/1.0 202 ACCEPTED
    Date: Fri, 20 May 2011 07:13:21 GMT
    Server: WSGIServer/0.1 Python/2.7
    Content-Length: 0
    Content-Type: text/html; charset=utf-8

Deleting Data
=============

No CRUD setup would be complete without the ability to delete resources/objects.
Deleting also requires significantly less complicated requests than
``POST``/``PUT``.


Deleting A Single Resource
--------------------------

We've decided that we don't like the provider we added & edited earlier. Let's
delete it (but leave the other objects alone)::

    curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/provider/884c0999-0f23-4670-bea6-eb1e58c2e9cd/

Once again, we get back the "Accepted" response of a 204::

    HTTP/1.0 204 NO CONTENT
    Date: Fri, 20 May 2011 07:28:01 GMT
    Server: WSGIServer/0.1 Python/2.7
    Content-Length: 0
    Content-Type: text/html; charset=utf-8


We can also use service_areas model api in above format
-------------------------------------------------------

Filtering of Service Areas
--------------------------

We can filter using any standard GeoDjango `spatial lookup <https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoquerysets/#spatial-lookups>`_ filter.  Simply provide a GeoJSON (or the analog) as a ``GET`` parameter value.

Let's find all of our ``GeoNote`` resources that contain a point inside
of `Golden Gate Park <https://sf.localwiki.org/Golden_Gate_Park>`_::

    /api/v1/service_areas/?geom__contains={"type": "Point", "coordinates": [-122.475233, 37.768617]}

Returns::

    {
        "meta": {
            "limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1},
        "objects": [
            {
                "content": "My note content",
                "id": "1",
                "polys": {
                    "coordinates": [[[
                        [-122.511067, 37.771276], [-122.510037, 37.766390999999999],
                        [-122.510037, 37.763812999999999], [-122.456822, 37.765847999999998],
                        [-122.45296, 37.766458999999998], [-122.454848, 37.773989999999998],
                        [-122.475362, 37.773040000000002], [-122.511067, 37.771276]
                    ]]],
                    "type": "MultiPolygon"
                },
                "resource_uri": "/api/geonotes/1/"
            }
        ]
    }

We get back the ``GeoNote`` resource defining Golden Gate Park.
Awesome!

Not Satisfied yet? Go to localhost homepage for more API details.
