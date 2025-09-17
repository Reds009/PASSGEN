import random
import time

a = '''       THIS IS PASSGEN A PROGRAM DESIGNED TO GENERATE PASSWORD FROM YOUR DESIRED LENGTH 
       USING DIFFERENT CHARACTERS AND SYMBOLS TO GENERATE STRONG PASSWORDS TO USE LATER
       CREATED BY REDS009\n'''
print(a)
current_version = "0.0.1"
check_version = str(input("[*] TYPE VERSION TO GET THE CURRENT VERSION OF PASSGEN OR TYPE EXIT TO CLOSE THE PROGRAM:     "))

if check_version == 'version' or 'VERSION':
    print(f"THE CURRENT VERSION OF PASSGEN IS '{current_version}'")

elif check_version == 'exit' or 'EXIT':
    print("CLOSING THE PROGRAM...")
    time.sleep(2)

else:
    print("INVALID COMMAND!")

# DECLARING THE PASSGEN VARIABLE AS AN EMPTY LIST!
passgen = []

# CHARACTERISTIC OF THE PASSWORD!
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "&é'(-è_çà)=/*-+.<>§!:;?,%ù£$µ*^¨"

# PRE-BUILDING THE PASSGEN!
passgen.append(random.choice(characters))
passgen.append(random.choice(numbers))
passgen.append(random.choice(symbols))

all_char = str(characters)+numbers+symbols
length = int(input("[*] ENTER THE LENGTH OF YOUR PASSWORD:  "))

if length < 8:
    print("[*] ERROR THE MINIMUM LENGTH MUST BE AT LEAST 8")
    time.sleep(5)
    length = 8

for temp in range(length - 3):
    passgen.append(random.choice(all_char))

passgen = "".join(passgen)
print("[*] PASSGEN IS CREATING YOUR PASSWORD...")
time.sleep(4)

print(f"[*] YOUR GENERATED PASSWORD IS\n\n{passgen}")