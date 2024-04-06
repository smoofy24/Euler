import math

def is_prime(n):

    # Cycle through
    for i in range(2, int(math.sqrt(n))+1):
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

def gen_erath_sieve(size_of_sieve):
    
    sieve_sqrt = math.sqrt(size_of_sieve)
    # Initiante sieve
    sieve = [2]
    for num in range(3, size_of_sieve, 2):
        sieve.append(num)
    
    # Start sieving
    for val in sieve:
        if val >= sieve_sqrt:
            break
        if val == 2:
            continue
        tmp = 2
        test = 0
        while test <= size_of_sieve:
            test = val*tmp
            if test in sieve:
                sieve.remove(test)
            tmp = tmp + 1

    return sieve

def get_fracts(num):
    
    fracts = []
    
    tmp = num
    for i in range(2, math.ceil(num/2)+1):
        while tmp%i == 0: 
            fracts.append(int(i))
            tmp = tmp/i
             
    return fracts
