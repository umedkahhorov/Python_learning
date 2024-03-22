# prime : factors only 1 and itself
from typing import List
from math import isqrt
import itertools

def list_primes(n: int) -> List[bool]:
    # Initialize a list of boolean values, where True indicates a prime number.
    out: List[bool] = [True] * (n + 1)
    out[0] = out[1] = False  # 0 and 1 are not prime numbers.

    # Sieve of Eratosthenes algorithm to mark non-prime numbers.
    for i in range(isqrt(n) + 1):
        if out[i]:
            for j in range(i * i, len(out), i):
                out[j] = False
    return out
def prime_check(n: int) -> bool:
    if n <=1:
        return False
    elif n<=3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,isqrt(n)+1,2):
            if n % i == 0:
                return False
        return True
"""
FUNCTION prime_check(n)
    IF n is less than or equal to 1
        RETURN False
    ELSE IF n is less than or equal to 3
        RETURN True
    ELSE IF n is divisible by 2
        RETURN False
    ELSE
        FOR each odd number i from 3 to the square root of n
            IF n is divisible by i
                RETURN False
        RETURN True
END FUNCTION
"""
######
def compute():
    out = max(((a,b) for a in range(-999,1000) for b in range(2,1000)), key=count_primes)
    return out[0]*out[1]
# This function counts the number of primes generated by the quadratic formula n^2 + an + b.
def count_primes(ab):
    a,b = ab
    for i in itertools.count():
        n = i*i + i*a+b
        if not is_prime(n):
            return i
isprimecache = list_primes(1000)
def is_prime(n):
    if n<0:
        return False
    elif n < len(isprimecache):
        return isprimecache[n]
    else:
        return prime_check(n)
if __name__ == "__main__":
    print (compute())
