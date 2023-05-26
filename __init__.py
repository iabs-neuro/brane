import git
import os
import stat
import pathlib

def custom_rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)


IMPORT_REPOS = []

extpath = os.path.join(pathlib.Path(__file__).parent.resolve(), 'externals')
os.makedirs(extpath, exist_ok=True)

for repo in IMPORT_REPOS:
    rppath = os.path.join(extpath, repo)
    if repo in os.listdir(extpath):
        custom_rmtree(rppath)

    rp = git.Repo.clone_from(f'https://github.com/iabs-neuro/{repo}',
                             rppath,
                             branch='main'
    )

from .externals.driada import *