#!/usr/bin/env python3

'''  
Integer Objects
    To gain practice, complete your python script with the following features:
        The script should have a Shebang line.
        The script should have an object called name
        The script should have an object called age
        The value of the name object should be Isaac
        The object age should contain a integer
        The value of the age object should be 72
        The script, when executed, should print out "Isaac is 72 years old!"
        Example run:

cd ~/ops445/lab1/
./lab1c.py
Isaac is 72 years old!
'''

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

#Define variables name & age
name = "Isaac"
age =72

#Print the message
print(name + ' is ' + str(age) + ' years old!')
