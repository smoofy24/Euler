import math
import mylib

def common_data(list1, list2):
    result = False
 
    # traverse in the 1st list
    for x in list1:
 
        # traverse in the 2nd list
        for y in list2:
   
            # if one common
            if x == y:
                result = True
                return result
                 
    return result

def get_prime_factors(num):
    fracts = []
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0 and mylib.is_prime(i):
            fracts.append(i)
    return fracts

dic = {}
prev_factors = []
cnt = 0
for i in range(1, 10000000):
    dic[i] = get_prime_factors(i)

    for j in dic.keys():
        if j == i:
            continue
        if common_data(dic[i],dic[j]):
            dic = {}
            break
    
    if len(dic) == 4:
        print(dic)

