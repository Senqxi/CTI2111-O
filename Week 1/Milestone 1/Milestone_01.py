# Edwin Arzu 
# Milestone 1
# 02/11/2024

import os
import time

print('Hello, I\'f you are using this program you want to introduce yourself to our classmates this year, I can help you with that! Just answer a few questions for me')
Answer = input('Are you ready?[y/n]')
y = 'Yes'
n = 'No'
if Answer == 'n':
    print('Looks like you got this yourself! Get\'em tiger')
elif Answer == 'y':
    print('Great! Let us begin.')
    os.system('clear')
name = input("What is your name? ")
print("Hello", name + "!")
time.sleep(2)
os.system('clear')
age = input('How old are you? ')
time.sleep(1)
os.system('clear')
Fav_Sport = input('What is your favorite sport? ')
time.sleep(1)
os.system('clear')
Fav_Book = input('What is your favorite Book? ')
time.sleep(1)
os.system('clear')
print('Thank you for answering all the questions! Lets gather your responses.')
time.sleep(2)
os.system('clear')
print('Generating.')
time.sleep(1)
os.system('clear')
print('Generating..')
time.sleep(1)
os.system('clear')
print('Generating...')
time.sleep(1)
os.system('clear')
print(f'Hello everyone, my name is {name} and I\'m {age} years old. My favorite sport is {Fav_Sport} and I enjoy reading {Fav_Book}')
