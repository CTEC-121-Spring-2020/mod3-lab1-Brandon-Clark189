"""
CTEC 121
Brandon Norton
Module 3 Lab 1
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    # conditional Expressions

    '''
    #Literals
    print("\nBoolean literals")
    print(True)
    print(False)
    print(type(True))
    print()

    # Relational operators
    print("Relational operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 != 5", 3 != 5)
    print()

    # using variables
    x = 3
    y = 5
    print("using variables")
    print("x:", x, "y:", y)
    print("x < y", x < y)
    print("x != y", x != y)
    print()

    # simple if statement

    print("x:", x, "y:", y)
    if x < y:
        print("x > y")

    if x > y:
        print("x > y")

    print("end simple if example")
    print()

    # If/else statement
    print("if/else statement")
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    x = 6
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")
    
    # Exercise 3-1
    for i in range(1, 11):
        if (i % 2) == 0:
            outputString = "even"
        else:
            outputString = "odd"
        print(i, outputString)
    print()
    
    # alphabetize names
    name = "Brandon"
    firstletter = "B"

    print("Multi-way if example")
    if firstletter == "A":
        print(name)
    elif firstletter == "B":
        print(name)
    elif firstletter == "C":
        print(name)
    # etc...
    elif firstletter == "Y":
        print(name)
    else:       #default case: name starts with Z
        print(name)
    print()
    '''

try:
    print(4/0)
except:
    print("\nThere was a divide by zero error. You can't divide by zero dummy.\n")
    exit()
main()    