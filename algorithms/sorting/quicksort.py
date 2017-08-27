from __future__ import print_function


def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, left, right):
    if left >= right:
        return

    pivot = partition(arr, left, right)

    quicksort_helper(arr, left, pivot - 1)
    quicksort_helper(arr, pivot + 1, right)


def partition(nums, left, right):
    # if using random init pivot, switch to the left anyway
    pivot_val = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot_val:
            right -= 1
        # the smaller number take the init pivot's place
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot_val:
            left += 1
        # the bigger number move to the right side
        nums[right] = nums[left]
    # the pivot move to where it should be
    nums[left] = pivot_val
    return left


if __name__ == '__main__':
    arr = [7, 5, 8, 2, 4, 3, 9, 1]
    quicksort(arr)
    print(arr)

    arr_with_dup = [3, 4, 2, 7, 3, 6, 8, 2]
    quicksort(arr_with_dup)
    print(arr_with_dup)
