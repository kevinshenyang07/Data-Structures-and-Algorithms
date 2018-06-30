#
# Permutations & Combinations

def subsets(nums):
    results = [[]]
    for num in sorted(nums):
        results += [item + [num] for item in results]
    return results


def subsets_dfs(nums):
    def dfs(depth, start, path):
        # if nums contain duplicates, check if path in results
        # before append
        results.append(path)
        if depth == len(nums):
            return
        # construct dfs calls by level
        for i in range(start, len(nums)):
            # later numbers get less options
            dfs(depth + 1, i + 1, path + [nums[i]])
    nums.sort()
    results = []
    dfs(0, 0, [])
    return results


#
# Two Pointers

# all problems involving partition / swapping
def partition(nums, start, end):
    # if using random init pivot, swap to the left anyway
    pivot_val = nums[start]
    left = start + 1
    right = end
    # let right cross left to make sure nums[right] < pivot_val in the end
    # left equal to right covers the two elements situation
    while left <= right:
        if nums[left] <= pivot_val:
            left += 1
        elif nums[right] >= pivot_val:
            right -= 1
        # if two pointers haven't crossed yet and ready to swap
        else:
            nums[left], nums[right] = nums[right], nums[left]
    # swap pivot with the rightmost element that is smaller than pivot
    nums[start], nums[right] = nums[right], nums[start]
    return right


#
# Linked List

def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def split(head):
    # assume at least one node
    # zero node situation should be checked before calling
    slow = fast = head
    # while there are at least two more nodes
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None  # avoid cycle
    return head, mid