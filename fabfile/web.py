from fabric.api import run, task, roles, sudo, env

import repo
import common
import context_managers

@task
@roles('web')
def update(branch=None):
    repo.update(branch)
    with context_managers.django(common.path('repo')):
        run('pip install -r requirements/{}.txt'.format(env.environment))

@task
@roles('web')
def stop():
    if env.environment == 'development':
        return
    sudo('stop app_gunicorn')

@task
@roles('web')
def start():
    if env.environment == 'development':
        return
    repo.clean_pyc()
    sudo('start app_gunicorn')

@task
@roles('web')
def restart():
    if env.environment == 'development':
        return
    stop()
    start()

@task
@roles('web')
def manage(*args):
    with context_managers.django(common.path('web')):
        run('python manage.py %s' % ' '.join('"%s"' % arg for arg in args))

@task
@roles('web')
def collectstatic():
    manage('collectstatic', '--noinput')
