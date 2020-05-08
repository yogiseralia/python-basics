Packages
--------
- Packages are directories 
- Modules are files
- Difference while using both is that ``package.__path__`` will return a valid absolute directory path, where else this is not present for module.

Import sys.path
----
- sys.path is python's own path list of packages that are installed with python.
  ````python
  import sys
  print(sys.path)
  ````
  OUTPUT-
  ````text
  ['', 'C:\\Program Files (x86)\\Python38-32\\python38.zip', 'C:\\Program Files (x86)\\Python38-32\\DLLs', 'C:\\Program Files (x86)\\Python38-32\\lib', 
  'C:\\Program Files (x86)\\Python38-32', 'C:\\Users\\USERNAME\\AppData\\Roaming\\Python\\Python38\\site-packages', 
  'C:\\Program Files (x86)\\Python38-32\\lib\\site-packages']
  ````
  Now as we can see this list can be traversed, and we can our own directory to this list for python be able to discover our package.
  
  Here we have created a directory ``not_searched`` with a ``path_test.py``, Now we will attempt to add it to sys.path and make it accessible.
  
   ````python
    >>> import path_test
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'path_test'
    >>> import sys
    >>> sys.path.append('not_searched')
    >>> import path_test
    >>> path_test.found()
    Python found me!
  ````