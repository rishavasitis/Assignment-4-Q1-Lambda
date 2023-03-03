#Q 1 Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

arg1=int(input('Enter the Number to add 25 in it: '))
add = lambda a : a + 25
print ('Answer >>>>',arg1 , '+ 25 =', add(arg1))

#lambda argument(s) : expression
#lambda is a keyword in Python for defining the anonymous function.
#anonymous function does not have a return keyword
#thats why automatically return the result of the expression in the function once it is executed