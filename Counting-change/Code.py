from cs50 import get_float
from math import floor

def main():
    while True:
        b=get_float("Change owed: ")
        a = floor(b * 100)


        if a>0:
            break

    quarters = a // 25
    dimes = (a % 25) // 10
    nickels = ((a % 25) % 10) // 5
    pennies = ((a % 25) % 10) % 5

    print("",quarters+dimes+nickels+pennies)

if __name__== "__main__":
    main()
