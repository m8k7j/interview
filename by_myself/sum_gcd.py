#!/usr/bin/env python
# coding=utf-8

"""
约数之和
数字等于它的约数之和
6=1+2+3
"""

def gcd(n):
    result = []
    for i in range(1,n):
        if n % i == 0:
            result.append(i)
    return result

def sum_gcd(n):
    result = gcd(n)
    summary = 0
    for i in result:
        summary += i
    if summary == n:
        return True
    else:
        return False

if __name__ == '__main__':
    for i in range(1,100):
        if sum_gcd(i):
            print i



