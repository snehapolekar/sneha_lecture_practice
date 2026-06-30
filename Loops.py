# while loop

# Print number 1 to 5
'''
i = 1

while i <= 5:
    print(i)
    i += 1

i = 5

while i >= 1:
    print(i)
    i -= 1

'''
# For loop

# Print number 1  to 5
'''
print("====for loop ====")

for i in range(1,6):
    print(i)

print("==== string loop ====")


name = "Python"

for i in name:
    print (i)


print("====loop through list ====")

fruits = ("Apple","Banana","mango","Orange")

for item in fruits:
    print(item)

print("="*20)


#Range() function

#range(Start,stop,step)

for i in range (5):
    print(i)

print("="*30)

for i in range(0,10,2):
    print(i)

print("="*20)

for i in range (10,0,-1):
    print(i)


'''

# Nested Loops in python

for i in range(1,5):
    for j in range(1,4):
        print(j,end="")
    print()


# Stops the loop immediately

for i in range(1,7):
    if i == 4:
        break
    print(i)


print("==== continue Statement ====")

# skip current iterations.

for i in range(1,7):
    if i == 5:
        continue
    print(i)


print("==== Pass Statement ====")

# skip current iterations.

for i in range(1,7):
    if i == 5:
        pass
    print(i)

    
        
   

    






















