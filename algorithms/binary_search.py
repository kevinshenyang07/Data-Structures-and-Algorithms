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
    

# Median of Two Sorted Arrays (hard but classic)
# do it in O(log(m+n)) time
def find_median_sorted_arrays(nums1, nums2):
    length = len(nums1) + len(nums2)
    if length % 2 == 1:
        return find_kth(nums1, nums2, length // 2)
    else:
        mid_left = find_kth(nums1, nums2, length // 2 - 1) 
        mid_right = find_kth(nums1, nums2, length // 2)
        return (mid_left + mid_right) / 2.0


# each call cuts the shorter array by half of its size
def find_kth(nums1, nums2, k):
    # swap to make sure k falls into nums2
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    if not nums1:
        return nums2[k]

    if k == len(nums1) + len(nums2) - 1:
        return max(nums1[-1], nums2[-1])
    # use k - i instead of len(nums2) to cover situation
    # when length % 2 == 0, same idea though
    i = len(nums1) // 2
    j = k - i
    if nums1[i] > nums2[j]:
        # get rid of right half of nums1 and right half of nums2
        # but why k == i?
        return find_kth(nums1[:i], nums2[j:], i)
    else:
        return find_kth(nums1[i:], nums2[:j], j)
