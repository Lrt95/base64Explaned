""" Module Exercice

Created by Antony Correia
Python Docstring
"""
def listToString(list):
    result = "".join(list)
    return(result)

def setMultipleOfString(str, mult):
    while len(str) % mult != 0:
        str = str + '='
    return(str)

def main():
    """ Function Main"""
    myList = ['B', "ib", 'a', "bo"]
    myString = listToString(myList)
    myTabString = setMultipleOfString(myString, 4)
    print("Exercice 10: " + myString)
    print("Exercice 11: " + myTabString)

if __name__ == '__main__':
    main()

