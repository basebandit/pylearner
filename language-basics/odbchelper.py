# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Triple quotes signify a multi−line string. Everything between the start and end quotes is part of a single string,
# including carriage returns and other quote characters. You can use them anywhere, but you'll see them most often used
# when defining a doc string.


def build_connection_string(params):
    """Build a connection string from a dictionary of params.
    
    Returns a string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])


if __name__ == "__main__":
    myParams = {"server": "devmars",
                "database": "master",
                "uid": "ke",
                "pwd": "secret"
                }
    print build_connection_string(myParams)

# Python functions have attributes, and that those attributes are available at
# runtime.
# A function, like everything else in Python, is an object.

# >>> import odbchelper
# >>> params = {"server":"devmars", "database":"master", "uid":"ke", "pwd":"secret"}
# >>> print odbchelper.build_connection_string(params)
# server=mpilgrim;uid=sa;database=master;pwd=secret
# >>> print odbchelper.build_connection_string.__doc__
# Build a connection string from a dictionary
# Returns string.
# The first line imports the odbchelper program as a module −− a chunk of code that you can use
# interactively, or from a larger Python program.
