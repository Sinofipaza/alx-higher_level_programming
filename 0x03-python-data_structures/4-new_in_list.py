#!/usr/bin/python3
if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        new_list = []
        for i in my_list:
                new_list.append(i)
        new_list[idx] = element
        return new_list
