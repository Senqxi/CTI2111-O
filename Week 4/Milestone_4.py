
# [Edwin Arzu]
# [Sun March 3rd, 2024]
# [Python 3.11]
# [Milestone 4 - Guess the Number]

import os
import time
import random

magic_number = random.randint(1, 50)

os.system('Clear')
print("-" * 50)
print("H3llo and Welc0me to my game cal1ed Numberz!\n\n 1n thi5 game y0u gu3ss the number 6etween 1 - 50 \n But b3ware y0u on1y have 5 chances t0 succ3ed!".center(50))
print("-" * 50)

name = input("\nBef0re w3 start 3nter y0ur nam3: ")
os.system('Clear')

print("-" * 50)
print(f"W3lc0me {name.title()}".center(50))
print("-" * 50)
print("L3t Us Beg1n!".center(50))
print("Ch0ose Y0ur Num6er".center(47))

attempts = 0
print("-" * 50)

picks = []

while attempts < 5:
    try:
        guess = int(input("3nter Y0ur Gu3ss: "))
        
        if guess < 1 or guess > 50:
            print("Gu3ss must b3 6etween 1 - 50. Gu3ss again ")
            print("-" * 50)
            time.sleep(1.3)
            continue
            
        if guess in picks :
            print("y0u alr3dy ch00s3 th1s numb3r")
            print("-" * 50)
            time.sleep(0.7)
            continue
            
        picks.append(guess)
        attempts += 1
            
        if guess < magic_number:
            print("Y0ur gu3ss 1s t00 1ow.")
            print("-" * 50)
            time.sleep(1.3)
            
        elif guess > magic_number:
            print("Y0ur gu3ss 1s t00 h1gh.")
            print("-" * 50)
            time.sleep(1.3)
            
        else:
            print("-" * 50)
            print(f"C0ngratu1ati0ns,\n {name.title()}! Y0u gu3ssed the number {magic_number} c0rrect1y 1n [{attempts}] attempts.")
            print("-" * 50)
            break
    except ValueError:
        print("! ! ! Numbers must be in numeric format ! ! !")
        print("-" * 50)
        time.sleep(0.7)
else:
    print(f"S0rry, {name.title()}. Y0u are 0ut 0f chanc3s. The numb3r was {magic_number}.\n\t\t B3tter 1uck n3xt tim3!")