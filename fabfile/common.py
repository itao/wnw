ROOT = '/goma'

PATHS = {
    'root': ROOT,
    'repo': '{}/deploy'.format(ROOT),
    'web': '{}/deploy/web'.format(ROOT),
    'secret': '{}/secret'.format(ROOT),
    'venv': '{}/venv'.format(ROOT),
}

def path(root, *parts):
    return '/'.join([PATHS[root]] + list(parts))
