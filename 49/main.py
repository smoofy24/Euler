#!/usr/bin/env python

import mylib

def main():

    prime_list = {}
    tmp_list = {}
    diff = []

    # We are looking for 4 digit numbers that should be prime (odd)
    for i in range(1001,9999, 2):
        if mylib.is_prime(i):
            prime_list[i] = None

    # Sort the values
    for val in prime_list:
        tmp_val = [int(i) for i in str(val)]
        tmp_val.sort()
        prime_list[val] = tmp_val

    for i in prime_list.keys():
        
        val = ''.join(map(str, prime_list[i]))

        if val in tmp_list:
            tmp_list[val].append(i)
        else:
            tmp_list[val] = [i]

    for i in tmp_list.keys():
        if len(tmp_list[i]) < 3:
            continue

        for num in tmp_list[i]:
            if num + 3330 in tmp_list[i]:
                if num + 2*3330 in tmp_list[i]:
                    print(i)
                    print(tmp_list[i])
        diff = []
    #    for cnt in diff:
     #       if diff.count(cnt) >= 2:
      #          print(diff.count(cnt))


    
if __name__ == "__main__":
   main() 

