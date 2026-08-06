# Type() function

number = 100
name = "Rohan"
price = 99.09
status = True

print(type(number))
print(type(name))
print(type(price))
print(type(status))

class Student:
    pass

s = Student()

print(type(s))

# dir() function

print(dir(s))

# isinstance() function

class Student:
    pass

class Employee(Student):
    pass

s = Student()

print(isinstance(s , Student))
print(isinstance(s , Employee))

#help() function

class Student:
    """
    Student Class
    Used to student information
    """

    def study(self):
        """ Study Student Method"""
        pass

help(Student)


# E-commerce System

class Product:

    def __init__(self, product_id , name , price):

        self.product_id = product_id
        self.name = name
        self.__price = price

    # get method

    def get_price(self):
        return self.__price

    # set method

    def set_price(self , price):

        if price > 0:
            self.__price = price
            print("Price Updated Successfully!.")
        else:
            print("Invalid Price")


    def display(self):
        print("======== Product Details =======")
        print("Product Id : " , self.product_id)
        print("Product Name : " , self.name)
        print("Product Price : " , self.__price)

# child class

class Mobile(Product):

    def __init__(self , product_id , name , price ,brand , ram , storage):
        super().__init__(product_id , name , price)

        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display(self):

        super().display()

        print("Product Brand :", self.brand)
        print("Product RAM :", self.ram)
        print("Product Storage :", self.storage)

    def buy(self):
        print("Order Placed Successfully!!")
        print("Thank You for Shopping with us.")

#main function

mobile = Mobile(101 , "iphone 17" , 85000 , "Apple" , 16 , 256 )

while True:

    print("========== E-Commerce Menu =========")

    print("1. View Product")
    print("2. Check Price")
    print("3. Update Price")
    print("4. Buy Product")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        mobile.display()

    elif choice == 2:

        print("Current Price : \u20B9", mobile.get_price())

    elif choice == 3:

        new_price = float(input("Enter new price,:"))

        mobile.set_price(new_price)

    elif choice == 4:

        mobile.buy()

    elif choice == 5:

        print("Thank You!!!!.")
        break

    else:

        print("Invalid Choice")


    
    

























