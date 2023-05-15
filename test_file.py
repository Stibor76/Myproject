# This is a test python file for git training
# This is an app that is going to produce a list of prime numbers
import math
import sys
# This is a function that will check if a number is prime
def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
# This is the main function
num = int(input("Enter a number: "))

if is_prime(num) == True:
    print("The number is prime")
else:
    print("The number is not prime")




