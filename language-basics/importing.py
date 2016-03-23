# The Import Search Path
# Python looks in several places when you try to import a module.
# Specifically, it looks in all the directories defined in sys.path.
# This is just a list, and you can easily view it or modify it with standard list methods.
# >>> import sys
# >>> sys.path
# ['', '/usr/local/lib/python2.2', '/usr/local/lib/python2.2/plat−linux2',
# '/usr/local/lib/python2.2/lib−dynload', '/usr/local/lib/python2.2/site−packages',
# '/usr/local/lib/python2.2/site−packages/PIL', '/usr/local/lib/python2.2/site−packages/piddle']
# >>> sys
# <module 'sys' (built−in)>
# >>> sys.path.append('/my/new/path')

# Importing the sys module makes all of its functions and attributes available.
# sys.path is a list of directory names that constitute the current search path. (Yours will look different,
# depending on your operating system, what version of Python you're running, and where it was originally
# installed.) Python will look through these directories (in this order) for a .py file matching the module name
# you're trying to import.
# You can add a new directory to Python's search path at runtime by appending the directory name to
# sys.path, and then Python will look in that directory as well, whenever you try to import a module. The
# effect lasts as long as Python is running.
