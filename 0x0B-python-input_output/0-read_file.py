#!/usr/bin/python3
<<<<<<< HEAD

=======
>>>>>>> bf3d4729c23765fcbc1b273fdc94fcd2f861d0db
def read_file(filename=""):
    """ prints file contents """
    if filename == "":
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
