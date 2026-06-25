# Python Operators, Variable and Data types

'''
1.Aritmetic Operator
2.Assignment Operator
3.Comparision Operator
4.Logical Operater
5.Bitwise Operater
6.Tyep conversion
'''

a=10
b=20

print('addition:', a+b)
print('substaraction:',a-b)
print('Multiplication:', a*b)
print('Division:', a/b)
print('Modulus:',a%b)
print('Exponentiation:', a**b)
print('Floor division:', a//b)

# Assignment Operator

x = 5 #simple assignment

y = 3

x += y#x=x+y

print(x)
print(y)

x -= y

print(x)
print(y)

x /= y

print(x)
print(y)

x %= y

print(x)
print(y)

x **= y

print(x)
print(y)

x //= y

print(x)
print(y)

# Comparision Operator

x = 10
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)


# Logical Operator(and, or, not)

x = True
y = False
z = False

print(x and y)
print(y and z)
print(x or y)
print(y or z)
print(not x)
print(not y)

# Tyep conversion

'''

int()
float()
str()
tuple()
list()
set()
dict()

'''

num_str = "123"
print(type(num_str))
num_int = int(num_str)
print(type(num_int))
print(num_int+7)

# multiple assignment

x, y, z = 10, 20, 30

print(x, y, z)

a = 20
b = 21

print(id(a))
print(id(b))









































































