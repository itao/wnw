from fabric.api import env, task, execute

import web
import db

env.forward_agent = True
env.user = 'goma'
env.roledefs = {}

ENVIRONMENT_ALIASES = {
    'p': 'production',
    's': 'staging',
    'd': 'development',
    'v': 'development',
}

ROLEDEFS = {
    'development': {
        'web': ['goma@127.0.0.1:2222'],
        'db': ['goma@127.0.0.1:2222'],
    }
}

@task
def e(environment):
    environment = ENVIRONMENT_ALIASES.get(environment, environment)
    if environment not in ROLEDEFS:
        raise ValueError('%s must be one of %s' % (environment, ROLEDEFS.keys()))

    env.environment = environment
    env.roledefs = ROLEDEFS[environment]

@task
def deploy(branch=None):
    if len(env.roledefs) == 0:
        raise ValueError('You must define an environemnt using e:<env>')

    execute(web.update, branch)

    execute(web.stop)

    execute(db.sync)
    execute(db.migrate)

    execute(web.start)

def useless():
    web
    db
