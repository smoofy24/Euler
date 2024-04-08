from mylibs import mylib

def goldbach(a,exp):
    return a+2*exp**2
def gen_odd_np():
    cnt = 1
    while True:
        if not mylib.is_prime(cnt):
            yield cnt
        cnt += 2

def gen_primes(limit):
    cnt = 1
    while cnt <=limit:
        if mylib.is_prime(cnt):
            yield cnt
        cnt += 1

for value in gen_odd_np():
    #print(f"value={value}")
    sem = 0
    for prime in gen_primes(value-2):
        #print(f"prime={prime}")
        sum = 0
        exp = 1
        while sum < value:
            sum = goldbach(prime,exp)
            #print(f"sum={sum}")
            exp += 1
        if sum == value:
            #print(f"Hodnotu {value} lze napsat jako {prime}+2*{exp-1}^2")
            sem = 1
            break
    if sem == 0:
        print(f"Hodnotu {value} nelze zapsat jako blabla")