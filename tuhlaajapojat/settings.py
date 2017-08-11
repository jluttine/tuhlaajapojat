# Django settings for tuhlaajapojat project.

from sportsteam.settings.prod import *

DEBUG = os.getenv("TUHLAAJAPOJAT_DEBUG", "0").lower() not in [
    "0", "false", "off"
]

TEAM_NAME = 'FC Tuhlaajapojat'
TEAM_SLUG = 'tuhlaajapojat'
TEAM_TAG = 'Tuhlaajapojat'

ADMINS = (
    ('Jaakko Luttinen', 'jaakko.luttinen@iki.fi'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Use environment variable here..
        'NAME':  os.getenv("TUHLAAJAPOJAT_DATABASE_NAME", "/tmp/tuhlaajapojat.db")
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fi'

SITE_ID = 1

# Make this unique, and don't share it with anybody.
# Use environment variable here..
SECRET_KEY = os.getenv("TUHLAAJAPOJAT_SECRET_KEY", "foobar")

ALLOWED_HOSTS = ['*']
