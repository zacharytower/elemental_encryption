'''
element_dict.py

Has one function: element_dict_generate()
Generates dictionary, with keys of the atomic number
and values of the corresponding atomic symbol of that atomic number.

Keys are ints, values are strs.
'''

def element_dict_generate():
    elements_sorted_file = open('elements_sorted.txt','r')

    d = {} # RETURNED

    for i, line in enumerate(elements_sorted_file.readlines()):
        d[i + 1] = line.split()[0]

    return d