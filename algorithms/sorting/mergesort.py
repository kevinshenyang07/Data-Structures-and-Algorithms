def mergesort(arr):
    if len(arr) <= 1:
        return arr
    # divide
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    # conquer
    return merge(left, right)
# O(nlogn) time / worst case, O(n) space
# result is stable

def merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    return merged + left + right


if __name__ == '__main__':
    nums = [1, 5, 3, 2, 4, 2, 11, 7]
    assert mergesort(nums) == sorted(nums)