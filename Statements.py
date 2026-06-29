# Control flow in Python

# Statements in Python

'''

1. if statemente
2. if...else statemente
3. if...elif...else statemente
4. match statemente
5. Continue statemente
6. break statemente

'''

# The if statement executes a block of code only if the specified condition is True. if the condition is False, the code inside the if block is skipped.

'''
if condition:
   #code
'''

age = 20

if age >= 18:
    print("You are eligible to vote.")


# The if....else statement is used when there are two possible outcomes:
# if the condition is True, the if block executes.
# if the condition is False , the else block executes.

'''
if condition:
    # code(True)
else:
    #code(False)
'''

number = -5

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")


# if....elif....else statement

# if...elif..else statement is used when multiple condition need to be checked.

'''
if condition1:
    #code
elif condition2:
    #code
elif condition3:
    #code
else :
    #code

'''

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else :
    print("Fail")


# match-case satements

num1 = 10
num2 = 5

operator = "+"

match operator :

    case "+":

        print("Addition :", num1 + num2)

    case "-":

        print("Substraction :", num1 - num2)
        
    case "*":

        print("Multiplication :", num1 * num2)
        
    case "/":

        print("Division :", num1 / num2)
        
    case _:

        print("invalid operator")


# Multiple values in one case use

char = "a"

match char :

    case "a"|"e"|"i"|"o"|"u":
        print("vowel")

    case _:
        print("consonents")


























    
