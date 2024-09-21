###Create a new file as primemodule.py that includes the following functions:
#- is_prime(n): returns True if n is a prime number, False otherwise
#- print_primes(n): prints all prime numbers less than n
#- get_primes(n): returns a list of all prime numbers less than n


def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    for i in range(n):
        if is_prime(i):
            print(i)

            
def get_primes(n):
    primes_list = []
    for i in range(n):
        if is_prime(i):
            primes_list.append(i)
    print(primes_list)
    return primes_list