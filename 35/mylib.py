import math

#
# Returns True if prime
#         False if not  prime
def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

#
# Reverses given number
#
def reverse(num):
  reversed_num = 0
  while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  return reversed_num   

#
# Generate sieve of Erathosenes
#
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

#
# Get list of fractions of number
#
def get_fracts(num):
    
    fracts = []
    
    tmp = num
    for i in range(2, math.ceil(num/2)+1):
        while tmp%i == 0: 
            fracts.append(int(i))
            tmp = tmp/i
             
    return fracts

#
# Shift number
#
def shift_number(number, direction="right", step=1):
    
    # Count digits
    tmp_num = number
    count = 0
    while tmp_num != 0:
        tmp_num //= 10
        count += 1

    tmp_num = number
    match direction:
        case "right":
            for i in range(0, step):
                tmp_num %= 10
                number = tmp_num * pow(10, count-1) + number//10 
                tmp_num = number
        case "left":
            for i in range(0, step):
                tmp_num = number//pow(10,count-1)
                number = number%pow(10,count-1)*10 + tmp_num
                tmp_num = number

    return number

#
# Pandigital number
#
def is_pandigital(number):

    # Count digits
    tmp_num = number
    count = 0
    while tmp_num != 0:
        tmp_num //= 10
        count += 1

    list = {}
    for i in range(0, count):
        list[i+1] = 0

    tmp_num = number
    while tmp_num != 0:
        test_num = tmp_num % 10
        tmp_num = tmp_num // 10

        if test_num == 0:
            test_num = 10

        if test_num in list.keys():
            list[test_num] = list[test_num] + 1
        else:
            return False

    for value in list.keys():
        if list[value] != 1:
            return False
            
    return True
