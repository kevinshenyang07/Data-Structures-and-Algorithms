class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Linked List Cycle, return true or false
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Linked List Cycle II
# return the node where the cycle begins, or null if no cycle
def detect_cycle(head):
    slow, fast = head, head
    # loop until fast == None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


# assumption: no cycles anywhere
# do it in O(n) time and O(1) space
# retain the structure of each list after the function returns
def get_intersection_node(head1, head2):
    if not head1 or not head2:
        return None
    # get the tail of either list
    tail1 = head1
    while tail1.next:
        tail1 = tail1.next
    # make a cycle
    tail1.next = head2
    node_inter = detect_cycle(head1)
    # cut cycle
    tail1.next = None
    return node_inter


# assumption: no cycles anywhere
# do it in O(nlogn) time and O(1) space
# recursive calls of mergesort actually takes O(logn) space 
def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head
    # loop until fast == last node or the node before last node
    # to correctly find middle
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)

    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    # create a new head
    dummy = ListNode(0)
    head = dummy
    while left and right:
        # no need to cut the node than append to new list
        if left.val <= right.val:
            head.next = left
            left = left.next
        else:
            head.next = right
            right = right.next
        head = head.next
    # splice the remaining list
    head.next = left or right

    return dummy.next

