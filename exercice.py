""" Module Exercice

Created by Antony Correia
Python Docstring
"""
def listToString(list):
    result = "".join(list)
    print(result)

def main():
    """ Function Main"""
    myList = ['B', "ib", 'a', "bou"]
    listToString(myList)


if __name__ == '__main__':
    main()

