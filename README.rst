===========
django-moat
===========

Installation
------------

To install from source ::

    pip install -e git+https://github.com/amrox/django-moat#egg=django-moat

PyPi package coming soon.


Usage
-----

Add ``moat.middleware.MoatMiddleware`` to your ``MIDDLEWARE_CLASSES``::

    MIDDLEWARE_CLASSES = (
        # Existing middleware classes
        "moat.middleware.MoatMiddleware",
    )

``moat`` has several configuration variable you may put in your ``settings.py``

MOAT_ENABLED
    Enable or disable ``moat``. (True or False)
    
    MOAT_ENABLED = True

HTTP_AUTH_REALM 
    Set Basic Auth Realm
    
    HTTP_AUTH_REALM = 'App Staging'

MOAT_ALWAYS_ALLOW_VIEWS
    A list of views to allow through ``moat``

    MOAT_ALWAYS_ALLOW_VIEWS = ['myapp.views.home']
    
MOAT_ALWAYS_ALLOW_MODULES 
    A list of modules to allow through ``moat``

    MOAT_ALWAYS_ALLOW_MODULES = ['oauth_provider.views']

Acknowledgements
----------------

Code borrowed from:
- http://djangosnippets.org/snippets/1720/
- https://github.com/pragmaticbadger/django-privatebeta

`Ryan Balfanz <http://ryanbalfanz.net/>`_ for suggesting the name ``moat``.
