#!/usr/bin/env python3

'''  
Investigation 5 - Exploring on How to Get Python to do Math

To gain practice, complete your script with the following content and details:
        The script should have a Shebang line.
        The object x should contain a integer with the value 10
        The object y should contain a integer with the value 2
        The object z should contain a integer with the value 5
        The script, when executed, should print out "10 + 2 * 5 = 20" (the printout should change if the values in the objects change)

    Example run:

cd ~/ops445/lab1/
./lab1d.py
10 + 2 * 5 = 20
'''

#Define variables x, y, z as 10, 2 & 5 as Int
x = 10
y = 2
z = 5

#Print the message of the 10 + 2 * 5 = 20
print(str(x) + ' + ' + str(y) + ' * ' + str(z) + ' = ' + str(x + y * z))
