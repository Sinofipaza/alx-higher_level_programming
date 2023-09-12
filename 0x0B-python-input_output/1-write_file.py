#!/usr/bin/python3

def number_of_lines(filename=""):
    """ count lines in file """
    count = 0
    if filename == "":
        return count
    with open(filename, "r") as f:
        for l in f:
            count += 1
    return count

write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
