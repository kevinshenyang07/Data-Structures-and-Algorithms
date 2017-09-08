from __future__ import print_function


def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, start, end):
    if start >= end:
        return

    pivot = partition(arr, start, end)

    quicksort_helper(arr, start, pivot - 1)
    quicksort_helper(arr, pivot + 1, end)


# partition with two pointers, returns a partition index
def partition(nums, start, end):
    # if using random init pivot, swap to the left anyway
    pivot_val = nums[start]
    left = start + 1
    right = end
    # let right cross left to make sure nums[right] < pivot_val in the end
    # left equal to right covers the situation when start + 1 = end
    while left <= right:
        if nums[left] <= pivot_val:
            left += 1
        elif nums[right] >= pivot_val:
            right -= 1
        else:  # if two pointers haven't crossed yet and ready to swap
            nums[left], nums[right] = nums[right], nums[left]
    # swap pivot with the rightmost element that is smaller than pivot
    nums[start], nums[right] = nums[right], nums[start]
    return right


if __name__ == '__main__':
    arr = [7, 5, 8, 2, 4, 3, 9, 1]
    quicksort(arr)
    print(arr)

    arr_with_dup = [3, 4, 2, 7, 3, 6, 8, 2]
    quicksort(arr_with_dup)
    print(arr_with_dup)
