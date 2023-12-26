from distutils.core import setup
# import py2exe
import py2app

setup(
    options = {'py2app': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "main.py"}],
    zipfile = None
)