import git
import os
import stat

def custom_rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)


IMPORT_REPOS = ['driada']

os.makedirs('externals', exist_ok=True)

for repo in IMPORT_REPOS:
    if repo in os.listdir('externals'):
        custom_rmtree(f'externals/{repo}')

    rp = git.Repo.clone_from(f'https://github.com/iabs-neuro/{repo}',
                                f'externals/{repo}',
                                branch='main')

from externals.driada import *