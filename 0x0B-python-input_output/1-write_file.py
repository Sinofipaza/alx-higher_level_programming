#!/usr/bin/python3

def number_of_lines(filename=""):
    """ count lines in file """
    lines = 0
    with open(filename, "r") as f:
        for line in f:
		lines += 1
    return
