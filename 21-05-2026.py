# Python Basic Program

# 1. Print your name using in built-infunction input()

name = input("Enter your name : ")
print("My name is " , name)

# Simple calculator

a = int(input("Enter first value : "))
b = int(input("Enter second value : "))

print("Addition : " , a + b )
print("Substraction : " , a - b )
print("Multiplication : " , a * b)
print("Division : " , a / b )      

# Silly Sandwich Maker

bread = input("Choose your bread (white / brown) : ")
filling = input("Choose your filling (cheese / jelly / banana) : ")

print("Here's your silly sandwich. ")
print("[" + bread +"bread +" + filling + " + rainbow glitter]")

# Rock , Paper , Scissors

import  random

choices = ["rock" , "paper" , "scissors"]
computer = random.choice(choices)

player = input("choose rock , paper or scissor : ")

print("computer choice : " , computer )

if player == computer :
    print("It's a tie.")
 elif (player == "rock" and computer == "scissors") or 
      (player == "paper" and computer == "rock") or 
      (player == "scissors" and computer == "paper'):
       print("You are win.")
 else:
     print("computer win")











      





















