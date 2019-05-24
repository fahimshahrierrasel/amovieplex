from .defaults import *

INSTALLED_APPS += [
    # Dependency of AllAuth
    "django.contrib.sites",
    # AllAuth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # Django Cripy Form
    "crispy_forms",
    # A Movie Plex Apps
    "movie",
    "theater",
    "frontend",
    "dashboard",
]

SITE_ID = 1

TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    # `allauth` needs this from django
    "django.template.context_processors.request"
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Media files (Uploaded Images, Docs)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Crispy From Customization
CRISPY_TEMPLATE_PACK = "bootstrap4"
