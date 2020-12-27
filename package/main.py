import os, sys

def local_import(argv=None):
    if argv is None:
        argv = sys.argv
    
    currentPath = os.getcwd()
    if currentPath not in sys.path:
        sys.path.append(currentPath)
    print(__import__(argv[1]))