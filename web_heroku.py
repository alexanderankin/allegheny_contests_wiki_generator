import subprocess

from script import main as script_main

def main():
    subprocess.Popen('heroku-php-nginx', shell=True)
    script_main()

if __name__ == '__main__':
    main()
