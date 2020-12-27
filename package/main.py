import sys
def local_import(argv=None):
    if argv is None:
        argv = sys.argv
    print(__import__(argv[1]))