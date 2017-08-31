# Merge Sorted Array
# assumption: nums1 has extra space to hold all the elements in nums
# m and n are the number of elements in these two static arrays
def merge(nums1, m, nums2, n):
    while m > 0:
        # starting from the right sides
        # index after m+n-1 to be the merged part
        if nums1[m - 1] < nums1[n - 1]:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
        else:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
    # if n == 0 then the pointer has moved n times
    # else nums has n elements smaller than all nums1 elements
    if n > 0:
        for i in range(n):
            nums1[i] = nums2[i]
        
