"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def prime_factors(n):
    result = ''
    for i in range(2, n + 1):
        num = 0
        while n % i == 0:
            num += 1
            n /= i
        if num > 0:
            result += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return result
