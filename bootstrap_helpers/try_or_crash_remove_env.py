import shutil

from . import MYENV_DIR

def try_or_crash_remove_env(env_dir=MYENV_DIR):
    try:
        shutil.rmtree(env_dir)
        print('Old environment found and cleaned up')
    except FileNotFoundError:
        print('No environment found to clean up')
    except NotADirectoryError:
        try:
            os.unlink(env_dir)
            print('Environment folder not a file and deleted')
        except:
            print('Environment folder not a file and couldn\'t be deleted')
            exit(1)
