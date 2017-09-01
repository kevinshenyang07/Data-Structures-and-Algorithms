


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