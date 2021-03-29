""" Module Exercice

Created by Antony Correia
Python Docstring
"""

""" Exercice 10 """


def listToString(list):
    result = "".join(list)
    return (result)


""" Exercice 11 """


def setMultipleOfString(str, mult):
    while len(str) % mult != 0:
        str = str + '='
    return (str)


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
  
def binary_to_decimal(binary_list):
    """ Function binary_to_decimal
    :param binary_list: binary's list
    :return: decimal's list
    """
    list_decimal = []
    for element in binary_list:
        list_decimal.append(int(element, 2))
    return list_decimal


def last_block(list):
    """Function last_block()
    add 0 for block have 6 characters"""
    for i in range(len(list)):
        if len(list[i]) < 6:
            list[i] = list[i] + "00"
    return list


def main():
    """ Function Main"""
    while True:
        inp = input("Add something to the list (leave empty to continue): ")
        if len(inp) == 0:
            break
        string_list = string_to_list(inp)
        print(string_list)
        list_ascii = character_to_ASCII(string_list)
        print(list_ascii)
        binary_list = ASCII_to_binary(list_ascii)
        print(binary_list)
        format_binary_list = add_zero(binary_list)
        print(format_binary_list)
        string_binary = concat_list_string(format_binary_list)
        print(string_binary)


if __name__ == '__main__':
    main()
