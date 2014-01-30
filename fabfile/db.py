from fabric.api import run, task, roles
from fabric.context_managers import settings

import context_managers as cm

@roles('db')
def needs_migration():
    with cm.django(), settings(warn_only=True):
        result = run('python manage.py migrate --list | grep "( )"')
        return result.return_code == 0

@task
@roles('db')
def sync():
    with cm.django():
        run('python manage.py syncdb --noinput')

@task
@roles('db')
def migrate():
    with cm.django():
        if needs_migration():
            run('python manage.py migrate')
        else:
            run('echo "nothing to migrate"')
