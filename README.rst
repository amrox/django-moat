===========
django-moat
===========

django-moat is a mini-app adds an additional layer of authentication via HTTP
Basic Auth. It's primary use case is to prevent access staging, development, or
otherwise private sites on the public internet. It is equivalent to configuring
Basic Auth on your webserver (Apache, nginx) but works in environments where
that is not possible (heroku).

Installation
------------

From PyPi ::

    pip install django-moat

To install from source ::

    pip install -e git+https://github.com/amrox/django-moat#egg=django-moat


Configuration
-------------

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

MOAT_DEBUG_DISABLE_HTTPS
    Disable HTTPS. *For testing purposes only.* Don't ship with this on.
        
        MOAT_DEBUG_DISABLE_HTTPS = True


Finally you may want to set the `SESSION_EXPIRE_AT_BROWSER_CLOSE <https://docs.djangoproject.com/en/1.3/ref/settings/#std:setting-SESSION_EXPIRE_AT_BROWSER_CLOSE>`_ setting.

Usage
-----

Your site now requires that your authenticate with a staff-level user before
accessing any non-whitelisted view. It is recommended that your add a dedicate
staff-level user in the django admin for moat authentication.

By default, the admin views will be blocked by ``moat``. You'll either need to
create a user with ``django-admin.py``, or add ``django.contrib.admin.sites``
to ``MOAT_ALWAYS_ALLOW_MODULES``.

Acknowledgements
----------------

Code borrowed from:

- http://djangosnippets.org/snippets/1720/
- https://github.com/pragmaticbadger/django-privatebeta

Thanks to `Ryan Balfanz <http://ryanbalfanz.net/>`_ for suggesting the name ``moat``.
