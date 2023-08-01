import os

ROOTDIR = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
cache = '/'.join([ROOTDIR, 'cache'])
staging = '/'.join([cache, 'staging'])
