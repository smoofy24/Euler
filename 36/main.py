from mylibs import mylib
LIMIT = 1000000
sum = 0

for num in range(1,LIMIT):
    binary = bin(num)[2:]
    if num == int(str(num)[::-1]) and binary == binary[::-1]:
        sum += num
        print(f"{num} is both way palindrome.")
print(f"Sum is {sum}.")