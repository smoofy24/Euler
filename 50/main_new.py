import sys

from mylibs import mylib

limit = 10000
total_count = 0
prime = 0
def sliding_window(sequence, window_size):
    for i in range(len(sequence) - window_size + 1):
        yield sequence[i:i + window_size]
def main():
    global limit,total_count,prime
    sieve = mylib.gen_erath_sieve(limit)
    #print(sieve)
    for window_len in range(2,len(sieve)):
        #print(f"Delka okna je {window_len}")
        for window in sliding_window(sieve, window_len):
            #print(f"Testuji okno {window}")
            window_sum = 0
            for i in window:
                window_sum += i
            if mylib.is_prime(window_sum):
                if window_len > total_count:
                    if window_sum < 1000000:
                        #print(f"Adding window {window} of {total_count} and sum {prime}.")
                        total_count = window_len
                        prime = window_sum

if __name__ == "__main__":
    main()
    print(f"Hodnota prvocisla je {prime} a pocet prvku je {total_count}")

