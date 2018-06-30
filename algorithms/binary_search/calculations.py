# Pow(x, n)
def my_pow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1  # 0 ^ 0 = 1
    if x == 0:
        return 0
    if n < 0:
        x = 1 / x
        n = -n
    # bottom up
    res = 1
    while n > 0:
        # pow(x, n) = pow(x * x, n // 2) * x if n is odd
        if n % 2 == 1:
            res = res * x
        x = x * x
        n = n // 2
    return res


# Sqrt(x)
def my_sqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x <= 1:
        return x
    l, r = 0, x
    while l + 1 < r:
        mid = l + (r - l) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            r = mid
        else:
            l = mid


# Divide Two Integers (return int)
# keep subtracting div from the remaining dividend and then doubling div
def divide(dividend, divisor):
    is_negative = (dividend < 0) ^ (divisor < 0)
    if dividend < 0:
        dividend = -dividend
    if divisor < 0:
        divisor = -divisor

    origin_divisor = divisor  # current divisor
    multipler = 1  # doubled div / divisor
    ans = 0
    while dividend >= origin_divisor:
        dividend -= divisor
        ans += multipler  # +1, +2, + 4...
        multipler += multipler
        divisor += divisor
        # start from the original divisor
        if dividend < divisor:
            divisor = origin_divisor
            multipler = 1
    if is_negative:
        return max(-ans, -2147483648)  # - 2 ^ 31
    else:
        return min(ans, 2147483647)  # (2 ^ 31 - 1) / 2
