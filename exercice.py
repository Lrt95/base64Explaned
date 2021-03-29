""" Module Exercice

Created by Antony Correia
Python Docstring
"""


def string_to_list(text):
    """ Function string_to_list
    transform string to list of characters"""
    my_list = []
    for character in text:
        my_list.append(character)
    return my_list


def character_to_ASCII(character_list):
    """Function character_to_ASCII
    transform characters to ASCII"""
    for i in range(len(character_list)):
        character_list[i] = ord(character_list[i])
    return character_list


def ASCII_to_binary(ASCII_list):
    """ Function ASCII_to_binary
    transform ASCII to binary"""
    for i in range(len(ASCII_list)):
        ASCII_list[i] = bin(ASCII_list[i])[2::1]
    return ASCII_list


def add_zero(binary_list):
    """add_zero
    add zero in first position"""
    for i in range(len(binary_list)):
        binary_list[i] = "0" + binary_list[i]
    return binary_list

def concat_list_string(list):
    list_res = ""
    for i in range(len(list)):
        list_res += list[i]
    return list_res


def my_split(string, number):
    return string[0: number]

def string_list(string):
    list_res = []
    string_res = ""
    index = 0
    for i in range(len(string)):
        string_res += string[i]
        index += 1
        if index >= 6:
            list_res.append(string_res)
            string_res = ""
            index = 0

    return list_res

if __name__ == '__main__':
    print(string_list(concat_list_string(add_zero(ASCII_to_binary(character_to_ASCII(string_to_list('ABCDE')))))))
