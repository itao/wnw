import sys

from fabric.api import run, task, env
from fabric.context_managers import cd
from fabric.contrib import files
from common import path

@task
def update(branch=None):
    # deployed repo is just a symlink to dev so do nothing
    if env.environment == "development":
        run("echo 'Skipping repo update because env=development'")
        return

    deploy_lock = path('home', 'run', 'deploy-lock.txt')
    if files.exists(deploy_lock):
        print 'Deploy lock exists. Aborting... If you want to remove this ' + \
            'then ssh onto the server and rm %s' % deploy_lock
        sys.exit(1)

    if branch is None:
        branch = "master"

    if not files.exists(path('repo')):
        run('git clone git@github.com:sesameio/goma.git %s' % path('repo'))

    with cd(path('repo')):
        run('git reset --hard HEAD')
        run('git fetch --all')
        run('git checkout origin/%s' % branch)

@task
def clean_pyc():
    with cd(path('repo')):
        run('find -name "*.pyc" | xargs rm -f')

@task
def version():
    with cd(path('repo')):
        run('git rev-parse HEAD')
