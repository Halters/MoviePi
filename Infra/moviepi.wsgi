#!/usr/bin/python
import sys
import os

def activate_venv(path):
    if sys.platform == 'win32':
        bin_dir = os.path.join(path, 'Scripts')
        site_packages = os.path.join(path, 'Lib', 'site-packages')
    else:
        bin_dir = os.path.join(path, 'bin')
        site_packages = os.path.join(
            path, 'lib', 'python%s' % sys.version[:3], 'site-packages')
    os.environ['PATH'] = bin_dir + os.pathsep + os.environ['PATH']
    prev_sys_path = list(sys.path)
    import site
    site.addsitedir(site_packages)
    sys.prefix, sys.real_prefix = path, sys.prefix

    # Move the added items to the front of the path:
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path

activate_venv("/var/www/FLASKAPPS/moviepiapi")
sys.path.insert(0, "/var/www/FLASKAPPS")

from moviepiapi import app as application
