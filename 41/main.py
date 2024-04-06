import mylib
from itertools import permutations

val = range(1,8)

perm_set = permutations(val)

for i in perm_set:
    if i[0] == 0:
        continue

    num = int(''.join(map(str, i)))
    if mylib.is_prime(num):
        print(num)
