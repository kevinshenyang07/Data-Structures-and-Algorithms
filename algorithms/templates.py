#
# Binary Search
# 二分法：保留有答案的那一半

# sorted array, no duplicates
# extra code so that it can also be used in finding leftmost target
# when there are duplicates
def binary_search(nums, target):
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2  # prevent int overflow
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid
        else:
            end = mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1


# rotated sorted array
def binary_search_rotated(nums, target):
    if not nums:  # empty list or None
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:  # make sure start and mid don't meet
        mid = start + (end - start) // 2  # prevent int overflow
        if nums[mid] == target:
            return mid
        if nums[start] < nums[mid]:  # mid is on the left half
            if nums[start] <= target <= nums[mid]:
                end = mid
            else:  # other wise cut from start to mid
                start = mid
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid
            else:
                end = mid
    # handle the cases when start = mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1


#
# Binary Tree

# preorder: root - left subtree - right subtree (root is pre-children)
# inorder: left subtree - root - right subtree (root is in-children)

def preorder(root):
    if not root:
        return []
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited


# DFS
def inorder(root):
    stack = []
    visited = []
    while root or stack:
        # to the most left node
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        visited.append(root.val)
        root = root.right
    return visited


def postorder(root):
    if not root:
        return []
    stack = [root]
    visited = []
    prev, curr = None, root
    while stack:
        curr = stack[-1]
        if not prev or prev.left == curr or prev.right == curr:
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
        elif prev == curr.left:
            if curr.right:
                satck.append(curr.right)
        else:
            visited.append(curr.val)
            stack.pop()
        prev = curr
    return visited


# Divide & Conquer
def LCA(root, node1, node2):
    # base case
    # if the traversal has reached the end
    # or one node is the root and another node is a child
    # or two nodes are
    if root is None or root == node1 or root = node2:
        return root

    # divide
    left = LCA(root.left, node1, node2)
    right = LCA(root.right, node1, node2)

    # conquer
    # if node1 and node2 are in different subtree
    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    return None


# Validate BST, 理解并背诵
def is_valid_bst(root):
    if not root:
        return True
    stack = []
    prev, curr = None, root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        # compare consecutive inorder nodes
        if prev and prev.val >= curr.val:
            return False
        prev = curr
        curr = curr.right  # go up if current node is not a root node
    return True


#
# BFS

# O(n) in time and space
def level_order(root):
    if not root:
        return []
    queue = [root]
    visited = []
    while queue:
        level = []
        size = len(queue)  # queue size changes within the loop
        for i in range(size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        visited += level
    return visited


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