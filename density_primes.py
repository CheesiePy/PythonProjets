"""
Student: May Lindenberg
ID: 203132949
Assignment no. 3
Program: density_primes.py
"""
import math
from random import *
Max = 10**9

def num_list_genarator():
    """this function retuns a list of 100K random integes in the spcifed range"""
    mylist = [randint(Max/2, Max) for i in range(100000)]
    return mylist

def is_prime(num):
    """return true if num is prime"""
    if(num%2 == 0):
        if(num != 2):
            return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if (num%i == 0):
            return False
    return True

def primelist(list1):
    """accepts a list and return a list of only the primes"""
    primelist = [i for i in list1 if is_prime(i)]
    return primelist

def main():
    x = num_list_genarator()
    num_of_primes = (len(primelist(x)))
    prime_density = (num_of_primes/100000)
    print("density of primes: ", prime_density)
    print("expected density:  ", 1/math.log(Max))
main()