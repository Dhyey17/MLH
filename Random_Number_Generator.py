import time


def RandomInt(x, y):
    sub = y - x
    random = int(time.time() * 1000)
    random %= sub
    random += x
    return random


def Random(x=0, y=10000):
    add = y + x
    random = time.time() * 1000
    random %= add
    random += x
    return random


while True:
    choice = int(input("1. Generate a random Integer(eg. 0,1,2,3.....)\n"
                       "2. Generate a random Float(eg. 0.2555, 1.764.....)\n"
                       "3. Exit"
                       "Enter your choice >>> "))
    if choice == 1:
        print("Enter the range")
        s = int(input("Starting range: "))
        e = int(input("Ending range: "))
        result = RandomInt(s, e)
        print(result)
    elif choice == 2:
        print("Enter the range")
        s = int(input("Starting range: "))
        e = int(input("Ending range: "))
        result = Random(s, e)
        print(result)
    
    else:
        exit()
