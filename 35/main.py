import mylib

MAX = 1000000

for i in range(2,MAX):
    prime = False
    if mylib.is_prime(i):
        prime = True
        # Count digits
        tmp_num = i
        count = 0
        while tmp_num != 0:
            tmp_num //= 10
            count += 1

        tmp_number = i
        for j in range(0, count-1):
            tmp_number = mylib.shift_number(tmp_number)
            #print("Testing ", i," with ",tmp_number)
            if not mylib.is_prime(tmp_number):
                prime = False
                break

    if prime:
        print("Number ",i,"is circulary prime.")
        
        
