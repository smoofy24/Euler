#!/usr/bin/env python3
"""
Module Docstring
"""
import math

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

def reverse(num):
  reversed_num = 0
  while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  return reversed_num

def main():
  sum = 0
  cnt = 0
  x = 3
  while cnt < 50:
    if is_prime(x):
      z = reverse(x)
      if is_prime(z) and z!=x:
        if x*x == reverse(z*z):
          cnt = cnt + 1
          sum = sum + x*x
          print(cnt,x,x*x,z*z,sum)
    x = x + 2
  print(sum)

if __name__ == "__main__":
  main()
