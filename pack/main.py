import importlib, os, sys

def local_import(argv=None):
    print("0.0.16")

    #currentPath = os.getcwd()
    #if currentPath not in sys.path:
    #    sys.path.append(currentPath)
    #else:
    #    print("current path in sys.path already!")

    print(sys.path)
    print(__import__(argv[1] if argv else sys.argv[1]))
