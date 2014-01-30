from contextlib import nested

from fabric.api import env
from fabric.context_managers import cd, prefix

from common import path

def django(path_=path('web')):
    return nested(
        cd(path_),
        prefix('export DJANGO_SETTINGS_MODULE=goma.settings.' + env.environment),
        prefix('source ' + path('secret', 'env')),
        prefix('source ' + path('venv', 'goma', 'bin', 'activate')),
    )
