# Sets , Dictionary  , Type Coversion , List of Dictionary

print("-"*40)
print("1. Set operations")
print("-"*40)

numbers = {1,2,3,4,5}

print(type(numbers))

numbers.add(6)

numbers.remove(3)

print("Is 2 present ?",2 in numbers )

print(numbers)

print("-" * 40)
print("2. Union , Intersection and Difference")
print("-" * 40)

set_a = {1,2,3,4}

set_b = {3,4,5,6}

print(set_a)
print(set_b)

print("Union:",set_a|set_b)
print("Intersection:",set_a & set_b)
print("Difference:",set_a - set_b)
print("Difference:",set_b - set_a)

print("=" * 40)
print("3. Dictionary Operations")
print("=" * 40)


student = {
    "name":"Rahul",
    "age":20,
    "grade":"A"
}

for key in student.keys():
    print(f"{key} : {student[key]}")

for value in student.values():
    print(value)

print(student['name'])

student["city"] = "Delhi"

student["age"] = 21

print(student)

del student["grade"]

print(student)

print("=" * 40)
print("4. Dictionary from Lists")
print("=" * 40)


keys = ['id' , 'name' , 'email']
values = [101 , 'Rajan' , 'example@gmail.com']

user = {}

for i in range(len(keys)):
    user[keys[i]] = values[i]

print(user)

print("=" * 40)
print("5. Type Conversion")
print("=" * 40)

num = '123'

print(type(num))

nums = int(num)

print(type(nums))

list_1 = [1 , 2 , 3 , 4]

tuple_1 = tuple(list_1)

print(tuple_1)

pairs = [(1 , "A") , (2 , "B")]

print(dict(pairs))














    


























