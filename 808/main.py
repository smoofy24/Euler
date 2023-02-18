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
      y = x*x
      z = reverse(y)
      s = math.sqrt(z)
      if not float.is_integer(s):
        x = x + 2
        continue
      if ((y != z) and (is_prime(x)) and (is_prime(s))):
        cnt = cnt + 1
        print(cnt,x,y,z,s)
        sum = sum + x
    x = x + 2
  print(sum)

if __name__ == "__main__":
  main()
