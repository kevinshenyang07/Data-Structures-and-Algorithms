# get prime numbers up to n (inclusive)
def sieve(n):
    # from 0 to n, but prime numbers start from 2
    is_prime = [True] * (n + 1)

    i = 2
    while i * i <= n:
        if is_prime[i]:
            # multiples of i must be non-prime numbers
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        i += 1

    primes = [i for i, val in enumerate(is_prime) if val and i >= 2]
    return primes
# O(nloglogn) time, O(n) space (proof is hard)


# factorization
# step 1: for every crossed number, record the 
# smallest prime that divides this number
def smallest_prime_divisors(n):
    divisors = [0] * (n + 1)
    i = 2
    while i * i <= n:
        if divisors[i] == 0:
            # same sieve method
            for j in range(i * 2, n + 1, i):
                # if has not been set yet
                if divisors[j] == 0:
                    divisors[j] = i
        i += 1
    return divisors
# f(10) returns [0,0,0,0,2,0,2,0,2,3,2 ]
#                   [2,3,4,5,6,7,8,9,10]        

# step 2: divide the number from right to left
def factorize(n):
    divisors = smallest_prime_divisors(n)
    prime_factors = []
    while divisors[n] > 0:
        prime_factors.append(divisors[n])
        n = n // divisors[n]
    prime_factors.append(n)
    return prime_factors


def gcd(a, b):
    # b cannot be 0
    if a % b == 0:
        return b
    return gcd(b, a % b)
# O(log(a+b)) time


if __name__ == '__main__':
    print sieve(10)
    print factorize(1024572)