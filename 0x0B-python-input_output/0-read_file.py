#!/usr/bin/python3
def read_file(filename=""):
    """ prints file contents """
    if filename == "":
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
