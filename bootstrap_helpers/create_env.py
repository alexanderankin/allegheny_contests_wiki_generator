# import venv
import virtualenv
import os

from . import MYENV_DIR

# def create_env(env_dir=MYENV_DIR):
#     venv.create(env_dir, system_site_packages=False, clear=True,
#                 symlinks=True, with_pip=True, prompt=None)

def create_env(env_dir=MYENV_DIR):
    virtualenv.create_environment(env_dir)

def use_env(env_dir=MYENV_DIR):
    p = os.path
    activator = p.join(env_dir, 'bin', 'activate_this.py')
    with open(activator) as f:
        exec(f.read(), {'__file__': activator})
