from __future__ import print_function


def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, start, end):
    if start < end:
       split_idx = partition(arr, start, end)

       quicksort_helper(arr, start, split_idx - 1)
       quicksort_helper(arr, split_idx + 1, end)


def partition(arr, start, end):
    pivot_val = arr[start]
    left = start + 1
    right = end

    # until the right mark crosses the left
    while left <= right:
        while left <= right and arr[left] <= pivot_val:
            left += 1
        while left <= right and arr[right] >= pivot_val:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    arr[start], arr[right] = arr[right], arr[start]

    return right


# time complexity O(nlogn), worst case O(n^2)
# result not stable


if __name__ == '__main__':
    arr = [7, 5, 8, 2, 4, 3, 9, 1]
    quicksort(arr)
    print(arr)

    arr_with_dup = [3, 4, 2, 7, 3, 6, 8, 2]
    quicksort(arr_with_dup)
    print(arr_with_dup)
