# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# build the reversed list from the end
def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def reverse_rec(head, prev=None):
    if not head:
        return prev
    node = head.next
    head.next = prev
    return reverse_rec(node, head)


# left half size >= right half size
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


def merge(left, right):
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
