import importlib, os, sys

def local_import(argv=None):
    print("0.0.12")
 
    print(importlib.import_module(argv[1] if argv else sys.argv[1]))
