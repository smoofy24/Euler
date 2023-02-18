#!/usr/bin/env python3
"""
Module Docstring
"""
import math

MAX = 100

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

  ###
  # Generate the prime list first
  cnt = 0
  x = 3
  prime_list = [2]
  while x < MAX:
    if is_prime(x):
      cnt = cnt + 1
      prime_list.append(x)    
    x = x + 2
  
  ###
  # Get the lenght
  list_len=len(prime_list)
  list_sum=sum(prime_list)
    
  ###
  # Count max
  cnt_max = 0
  num_max = 0

  cnt_a = 0
  cnt = 0
  while cnt_a < list_len-1:
    cnt_b = cnt_a
    tmp_sum = 0
    cnt = 0
    while cnt_b < list_len-1:
      tmp_sum = tmp_sum + prime_list[cnt_b]
      if is_prime(tmp_sum):
        cnt = cnt + 1
        if cnt_max < cnt:
          cnt_max = cnt
          num_max = tmp_sum
      cnt_b = cnt_b + 1
    cnt_a = cnt_a + 1
  print(cnt_max, num_max)
  

if __name__ == "__main__":
  main()
