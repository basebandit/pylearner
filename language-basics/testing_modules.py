# Testing Modules
# Python modules are objects and have several useful attributes. You can use this to easily test your modules as you
# write them using the if __name__ trick.

if __name__ == "__main__":
    pass

    # Replace pass with the function you want to test once this file is ran directly as a standalone program

    # Modules are objects, and all modules have a built−in attribute
    # __name__. A module's __name__ depends on how you're using the module. If you import the module, then
    # __name__ is the module's filename, without a directory path or file extension. But you can also run the module
    # directly as a standalone program, in which case __name__ will be a special default value, __main__.
    # >>> import odbchelper
    # >>> odbchelper.__name__
    # 'odbchelper'
    # Knowing this, you can design a test suite for your module within the module itself by putting it in this if
    # statement.
    # When you run the module directly, __name__ is __main__, so the test suite executes. When you import the
    # module, __name__ is something else, so the test suite is ignored. This makes it easier to develop and debug new
    # modules before integrating them into a larger program.
