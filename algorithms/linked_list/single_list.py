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


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


# reverse the list from mth to nth node, do it in-place and in one-pass
# note: 1 <= m <= n <= length of the list
def reverse_between(head, m, n):
    if m == n:
        return head
    # use dummy head whenever we need to modify the list
    dummy = ListNode(0)
    dummy.next = head
    head = dummy
    # the node before the part of the list to be reversed
    left = head
    for i in range(m - 1):
        left = left.next
    # reverse, one step for each node involved, hence (n - m + 1) times
    prev = None
    curr = left.next
    for i in range(n - m + 1):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # connect the start of the reversed list with 
    left.next = prev
    # connect the end of the reversed list to the start of the rest of the list
    left.next.next = curr
    return dummy.next


# reverse k nodes at a time, with k < size of the list
# if the length of a group of nodes is smaller than k, remain as is
# do it with constant space
def reverse_k_group(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    head = dummy
    # stop when there are less than k nodes
    while True:
        head = reverse_k_nodes(head, k)
        if not head:
            break
    return dummy.next


# head -> n1 -> n2 ... nk -> nk+1
# =>
# head -> nk -> nk-1 ... n1 -> nk+1
# return n1
def reverse_k_nodes(head, k):
    # iterated to kth node, stop if there are less than k nodes
    nk = head
    for i in range(k):
        if not nk:
            return None
        nk = nk.next
    # check the kth node
    if not nk:
        return None
    # get first node and the node after kth node
    n1 = head.next
    nkplus = nk.next
    # reverse these k nodes
    prev = None
    curr = n1
    while curr != nkplus:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # connect with the rest of linked list
    head.next = nk
    n1.next = nkplus
    return n1


# similar to clone graph, can have duplicate labels
# create new nodes when traversing through links, then copy the links
# O(n) time and space
def copy_random_list(head):
    if not head:
        return None
    mapping = {}  # original node => copied node
    mapping[head] = RandomListNode(head.label)
    
    curr = head
    while curr:
        if curr.next:
            if curr.next not in mapping:
                mapping[curr.next] = RandomListNode(curr.next.label)
            mapping[curr].next = mapping[curr.next]
        if curr.random:
            if curr.random not in mapping:
                mapping[curr.random] = RandomListNode(curr.random.label)
            mapping[curr].random = mapping[curr.random]
        curr = curr.next

    return mapping[head]
    
