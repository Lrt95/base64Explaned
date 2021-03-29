""" Module Exercice

Created by Antony Correia
Python Docstring
"""
import string


def listToString(list):
    """ Function List to String
    :param list:
    :return: string
    """
    result = "".join(list)
    return result


""" Exercice 11 """


def setMultipleOfString(str, multiple):
    """ Function set mutliple
    :param str: 
    :param multiple: 
    :return: string
    """
    while len(str) % multiple != 0:
        str = str + '='
    return str


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


def ASCII_to_binary(ascii_list):
    """ Function ASCII_to_binary
    transform ASCII to binary"""
    for i in range(len(ascii_list)):
        ascii_list[i] = bin(ascii_list[i])[2::1]
    return ascii_list


def add_zero(binary_list):
    """add_zero
    add zero in first position"""
    for i in range(len(binary_list)):
        binary_list[i] = "0" + binary_list[i]
    return binary_list


def concat_list_string(list):
    """  Function concat list
    :param list:
    :return:
    """
    list_res = ""
    for i in range(len(list)):
        list_res += list[i]
    return list_res


def string_list(string):
    """  Function transform string to list
    :param string:
    :return:
    """
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
    list_res.append(string_res)
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
    if len([len(list)]) < 6:
        my_list = list
        last_element = len(my_list) - 1
        while len(my_list[last_element]) < 6:
            my_list[last_element] += "0"
        return my_list


def encode_base_64(list):
    """ Function encode base 64 list

    :param list:
    :return: list base 64
    """
    table_base_64 = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
    list_result = []
    for element in list:
        list_result.append(table_base_64[element])
    return list_result


def main():
    """ Function Main"""
    while True:
        inp = input("Add something to the list (leave empty to continue): ")
        if len(inp) == 0:
            break
        string_list_temp = string_to_list(inp)
        list_ascii = character_to_ASCII(string_list_temp)
        binary_list = ASCII_to_binary(list_ascii)
        format_binary_list = add_zero(binary_list)
        string_binary = concat_list_string(format_binary_list)
        list_binary_6_digit = string_list(string_binary)
        list_of_8digit = last_block(list_binary_6_digit)
        binary_decimal = binary_to_decimal(list_of_8digit)
        base64 = encode_base_64(binary_decimal)
        string_base64 = listToString(base64)
        multiple_4 = setMultipleOfString(string_base64, 4)
        print(multiple_4)


if __name__ == '__main__':
    main()
