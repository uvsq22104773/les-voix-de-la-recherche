from distutils.core import setup
import py2exe

setup(
    options = {'py2exe' : {'bundle_files' : 1, 'compressed' : True}},
    windows = [{'script' : "La question mystère.py", 'icon_ressources' : [(0, '42v5.png')]}],
    zipfile = None
)