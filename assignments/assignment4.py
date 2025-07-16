def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def print_primes_desc(m, n):
    for i in range(n, m-1, -1):
        if is_prime(i):
            print(i, end=" ")

print_primes_desc(10, 30)
