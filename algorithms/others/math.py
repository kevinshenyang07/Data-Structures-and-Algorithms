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


# greatest common divisor
def gcd(a, b):
    # b cannot be 0
    if a % b == 0:
        return b
    return gcd(b, a % b)
# O(log(a+b)) time


# lowest common multiply
def lcm(a, b):
    return a * b / gcd(a, b)


# Mirror Reflection
# imagine the walls can be mirrored upward, each time the ray hit
# the left or right wall it goes up by q vertically
def mirror_reflection(p, q):
    lcm = lcm(p, q)

    if lcm / q % 2 == 0:
        return 2
    if lcm / p % 2 == 1:
        return 1
    if lcm / p % 2 != 1:
        return 0

# Find the Derangement of An Array
# a derangement is a permutation of the elements of a set,
# such that no element appears in its original position
# f(3) = 2
# the original array is [1,2,3], the two derangements are [2,3,1] and [3,1,2]
def find_derangement(n):
    if n == 1: return 0

    mod = 10 ** 9 + 7
    x, y = 1, 0  # D(2) = D(n-1), D(1) = D(n-2)
    for i in range(3, n + 1):
        z = (i - 1) * (x + y) % mod
        x, y = z, x
    return x
# Explanation:
# The first person has N-1 choices to put on a hat, say he wears hat X.
# Now consider what hat person X is wearing. Either he takes hat 1, and we have D(N-2) ways to
# arrange the remaining hats among people; or he doesn't take hat 1, which if we relabelled it as hat X,
# would have D(N-1) ways to arrange the remaining hats.
# D(n) = (n - 1) * (D(n - 1) + D(n - 2))


if __name__ == '__main__':
    print sieve(10)
    print factorize(1024572)
