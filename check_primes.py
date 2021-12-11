"""
Student: May Lindenberg
ID: 203132949
Assignment no. 5
Program: check_primes.py
"""

from random import randint

def get_even_odd_parts(n):
    """
    func: this func gets a n > 0, (n is a natural numbet) and return the even and odd prat of the number acouding to the formola:  n = 2**oddpartXevenpart
    param: n --> natural positiva number
    returns even_c --> the even part of n, odd_c --> the odd part of n
    """
    even_c = 0
    odd_c = 0
    c = n
    while n >= 1:
        if c % 2 == 0:
            if n % 2 == 0:
                even_c += 1
                n = n / 2
            elif n == 1:
                odd_c = 1
                break
            else:
                odd_c = c//2**even_c
                break
        else:
            odd_c = c
            break
    return even_c, odd_c


def is_probably_prime(n, num_iterations):
    """
    func: this func calls the get_even_odd_parts on n-1 and then calls the func is_suspected_prime "num_iterations" times
    param: n --> natural positive number
    param: num_itertaions --> natural positive number between 5-10
    returns: if all the calls of is_suspected_prime where true the func will return true else return False
    """
    s_t = get_even_odd_parts(n-1)
    s, t = s_t[0], s_t[1]
    for i in range(num_iterations):
        if not is_suspected_prime(n, t, s):
            return False
        return True

def is_suspected_prime(n, t, s):
    """
    func: takes the t and s given to us by the get_even_odd_parts functions
    param: n: natural positive number > 0, t = odd part of n, s = the even part of n
    returns: True or False if it think the number is prime
    """
    a = randint(2, n-1)
    d = modular_power(a, t, n)
    if d == 1 or d == n-1:
        return True
    for i in range(s-1):
        d = d**2 % n
        if d == n-1:
            return True
    return False

def modular_power(a, b, n):
    """ computes a**b (mod n) using iterated squaring
        assumes b is a nonnegative integer """
    lst = []
    while b > 0:
        if b % 2 == 1:
            lst = [1]+lst
        else:
            lst = [0]+lst
        b//=2
    result = 1
    for k in lst:
        result = (result**2) % n
        if k == 1:
            result = (result*a) % n
    return result


def main():
    input_file = "input_ex1.txt"  ## enter coustom file path to get difrent resoult
    output_file = "output_ex1.txt"
    with open(input_file, "r") as reader, open(output_file, "w") as writer:
        temp = reader.readlines()
        f = [int(i) for i in temp]
        for i in range(len(f)):
            if is_probably_prime(int(f[i]), 10):
                writer.write("{0} is prime".format(f[i]))
                writer.write("\n")
            else:
                writer.write("{0} is not prime".format(f[i]))
                writer.write("\n")
    reader.close()
    writer.close()
    print('Done! please check "{0}"'.format(output_file))
main()