#!/bin/python3

import math
import os
import random
import re
import sys

"""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""

start_message = "Please select a positive integer between 1 and 100"
error_message = "Invalid input"

def checkInput(n):
    if n < 1:
        print(error_message)
        return 0
    elif n > 100:
        print(error_message)
        return 0
    else:
        return 1

def weirdFunc(n):
    response1 = "Weird"
    response2 = "Not Weird"
    if n%2 != 0:
        return response1
    elif n>20:
        return response2
    elif n in range(2,6):
        return response2
    elif n in range(6,21):
        return response1

def main():
    print(start_message)
    n = int(input().strip())
    result = weirdFunc(n)
    print(result)

if __name__ == '__main__':
    main()
