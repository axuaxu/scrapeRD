__author__ = 'Anne'
import os
import django
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates').replace('\\', '/')]

print BASE_DIR, TEMPLATE_DIRS

print(django.get_version())
