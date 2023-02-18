import math

def is_prime(n):

    # Edge case - 1 is not a prime :)
    if n == 1:
        return False

    # 2 is the only even prime then we can do steps by 2 
    if n == 2:
        return True

    # Cycle through
    for i in range(3, int(math.sqrt(n))+1, 2):
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
