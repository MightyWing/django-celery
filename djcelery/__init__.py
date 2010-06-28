"""Django Celery Integration."""
import os

# Importing this module enables the Celery Django loader.
os.environ["CELERY_LOADER"] = "djcelery.loaders.DjangoLoader"

VERSION = (1, 1, 2)

__version__ = ".".join(map(str, VERSION[0:3])) + "".join(VERSION[3:])
__author__ = "Ask Solem"
__contact__ = "ask@celeryproject.org"
__homepage__ = "http://github.com/ask/django-celery/"
__docformat__ = "restructuredtext"


def is_stable_release():
    if len(VERSION) > 3 and isinstance(VERSION[3], basestring):
        return False
    return not VERSION[1] % 2


def version_with_meta():
    return "%s (%s)" % (__version__,
                        is_stable_release() and "stable" or "unstable")
