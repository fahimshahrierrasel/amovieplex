from .base import *

DEBUG = True

INSTALLED_APPS += [
    # Django Debug Toolbar
    "debug_toolbar",
    # Django Extensions
    "django_extensions",
]

MIDDLEWARE += [
    # Django Debug Toolbar Middleware
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

INTERNAL_IPS = ["127.0.0.1", "0.0.0.0"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
