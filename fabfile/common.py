HOME_ROOT = '/goma'
REPO_ROOT = '/goma/deploy'

PATHS = {
    'repo': REPO_ROOT,
    'root': HOME_ROOT,
    'web': '{}/web'.format(REPO_ROOT),
    'secret': '{}/secret'.format(REPO_ROOT),
    'venv': '{}/venv'.format(REPO_ROOT),
}

def path(root, *parts):
    return '/'.join([PATHS[root]] + list(parts))
