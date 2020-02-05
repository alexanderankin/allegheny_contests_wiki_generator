import os, subprocess, sys

def check_if_installed(name):
    try:
        __import__(name)
        return True
    except:
        return False

def install_list(packages):
    p = os.path
    install_command = [p.join(sys.prefix, 'bin', 'python'), '-m', 'pip', 'install']
    install_command.extend(packages)
    subprocess.check_call(install_command)

def install_missing(packages):
    missing_packages = []
    for package in packages:
        name, package_name = package
        if not check_if_installed(name):
            missing_packages.append(package_name)

    if len(missing_packages) > 0:
        install_list(missing_packages)
