MYENV_DIR = 'myenv'

from .try_or_crash_remove_env import try_or_crash_remove_env as remove_env

from .create_env import create_env
from .create_env import use_env

from .check_install import check_if_installed
from .check_install import install_list
from .check_install import install_missing
