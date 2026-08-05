#Python OOP Examples

# Class definition

# A class is a blueprint or template used to create objects.
# It defined what data and actions an object will have.
# Data : Attributed
# Actions : Methods

# House Bluperint

# Class = Blueprint / Design

# Object defination

# An object is a real instance of a class.

# It contains actual values and can use the methods defined in the class.

# Blueprint -> Honda , Audi, Tesla

# Object : Real thing

# Encapsulations

# Encpsulation means keeping data and methods together inside a class and protecting important data from direct access.

# ATM Machine -> Withdraw Cash -> Deposit Case

# Encapsulation = Data Protection +  Controlled Access
'''
class ClassName:
  pass

car = className()
'''
'''
1. Attributes
2. Constructor
3. Destructor
4. self keyword
'''

class car:

    # constructor

    def __init__(self, brand = None , model = None , color = None , price = None , name = None , age = None , dob = None , marks = None):

      # car
      self.brand = brand
      self.model = model
      self.color = color
      self.price = price

      # user
      self.name = name
      self.age = age
      self.dob = dob
      self.marks = marks


    # Method

    def start(self):
        print(f"{self.brand} {self.model} is Starting ...")

    #Method

    def car_details(self):
        print(f"""
        Brand : {self.brand}
        Model : {self.model}
        Color : {self.color}
        Price : {self.price}
        """)

    def user_details(self):
        print(f"""
        Name : {self.name}
        Age : {self.age}
        DOB : {self.dob}
        Marks : {self.marks}
        """)

car1 = car("Honda","Amaze","Black","10000","Sneha","17","26-02-2009",90)

car1.car_details()

class student:

    # constructor

    def __init__(self  ,name, age, dob, marks):


         # use
         self.name = name
         self.age = age
         self.dob = dob
         self.marks = marks

   

    def User_Details(self):
         print(f"""
         Name : {self.name}
         Age : {self.age}
         DOB : {self.dob}
         Marks : {self.marks}
         """)

student1 = student("Sneha",17,"26-02-2009",90)

student1.User_Details()

# simple creation

class person:

    pass

p1 = person()

print(type(p1))

class person:

    name = "sneha"

    age = 17

    course = "Python"

p1 = person()

print(p1.name)
print(p1.age)
print(p1.course)

# 1. Multiple Objects with Destructor
'''
class Customer:

  def __init__(self , name):
    self.name = name
    print(f"{self.name} logged in.")

  def shopping(self):
    print(f"{self.name} is shopping.")

  def __del__(self):
    print(f"{self.name} logged out.")

c1 = Customer("Rahul")
c2 = Customer("Priya")
c3 = Customer("Ronak")

c1.shopping()
c2.shopping()
c3.shopping()

del c1
del c2
del c3
'''
# Default Constructor  , Destructor
'''
class Employee:

  def __init__(self):
    self.name = "vivek"
    self.department = "IT"

    print(self.name , "joined office.")

  def display(self):
    print("Employee :" , self.name)
    print("Department : " , self.department)

  def __del__(self):
    print(self.name , "Left Office.")


emp = Employee()

emp.display()

del emp
'''
# Bank Account

class BankAccount:

  def __init__(self , account_holder , account_number , balance):
    self.account_holder = account_holder
    self.account_number = account_number
    self.__balance = balance # Private Variable

  def deposit(self , amount):

    if amount > 0:
      self.__balance += amount
      print(f"${amount} Deposited Successfully!.")

    else:
      print("Invalid amount.")


  def withdraw(self , amount):

    if amount <= 0:
      print("Invalid amount.")

    elif amount > self.__balance:
      print("Insufficient amount.")

    else:
      self.__balance -= amount
      print(f"${amount} withdraw Successfully!.")

  def check_balance(self):
    print(f"Current Balance : ${self.__balance}")

  def display(self):

    print("======= Account Details =======")

    print("Account Holder : " , self.account_holder)
    print("Account Number : " , self.account_number)
    print("Account Balance : " , self.__balance)


name = input("Enter Account Holder Name : ")
acc_num = int(input("Enter Account Number: "))
balance = float(input("Enter Opening amount: "))

account = BankAccount(name , acc_num , balance)

while True:

  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Display")
  print("5. Exit")

  choice = int(input("Enter your choice : "))

  if choice == 1:

    amount = float(input("Enter deposite amount : "))
    account.deposit(amount)

  elif choice == 2:

    amount = float(input("Enter withdraw amount : "))
    account.withdraw(amount)

  elif choice == 3:
    account.check_balance()

  elif choice == 4:
    account.display()

  elif choice == 5:
    print("Thank You!!!!")
    break

  else:
    print("Invalid Choice")
    






    










   
        
    




























