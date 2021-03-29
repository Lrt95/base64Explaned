""" Module Exercice

Created by Antony Correia
Python Docstring
"""

""" Exercice 10 """
def listToString(list):
    result = "".join(list)
    return(result)

""" Exercice 11 """
def setMultipleOfString(str, mult):
    while len(str) % mult != 0:
        str = str + '='
    return(str)

def main():
    """ Function Main"""
    myList = []
    while True:
        inp = input("Add something to the list (leave empty to continue): ")
        if len(inp) == 0:
            break
        myList.append(inp)
    myString = listToString(myList)
    myTabString = setMultipleOfString(myString, 4)
    print("Exercice 10: " + myString)
    print("Exercice 11: " + myTabString)

if __name__ == '__main__':
    main()

