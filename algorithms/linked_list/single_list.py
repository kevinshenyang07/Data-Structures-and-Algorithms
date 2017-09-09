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


def swap_pairs(head):
    # set up dummy node, which covers corner cases
    # where head is None or head.next is None
    dummy = ListNode(0)
    dummy.next = head
    head = dummy
    # while there is at least 2 nodes to handle
    while head.next and head.next.next:
        # give nodes one by one
        node1 = head.next
        node2 = node1.next
        node3 = node2.next
        # set link left to right
        head.next = node2
        node2.next = node1
        node1.next = node3
        # move pointer
        head = node1
    return dummy.next


# Remove Duplicates from Sorted List II
# example: 1->1->2->3 returns 2->3
def delete_duplicates(head):
    # set up dummy node
    dummy = ListNode(0)
    dummy.next = head
    head = dummy
    # while there is at least 2 nodes to handle
    # head and tail are nodes outside
    while head.next and head.next.next:
        curr_val = head.next.val
        tail = head.next.next
        # if there is duplicates, move tail forward
        while tail and tail.val == curr_val:
            tail = tail.next
        # if tail has been moved
        if head.next.next != tail:
            head.next = tail
        else:
            head = head.next
    return dummy.next


def add_two_numbers(l1, l2):
    carry = 0
    dummy = ListNode(0)
    head = dummy
    # until all nodes are visited and no new digit carried
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        sub_total = v1 + v2 + carry
        carry, mod = sub_total // 10, sub_total % 10
        head.next = ListNode(mod)
        head = head.next
    return dummy.next


# Partition List
# approach: maintain two queues, the first one stores all nodes with val
# less than x, the second queue stores the rest nodes
# finally, cut off extra nodes and concat these two queues
def partition(head, x):
    # dummy heads of two queues
    dummy1, dummy2 = ListNode(0), ListNode(0)
    # the end for each queue, extra nodes might follow
    curr1, curr2 = dummy1, dummy2
    while head:
        if head.val < x:
            curr1.next = head
            curr1 = head
        else:
            curr2.next = head
            curr2 = head
        head = head.next
    # splice two queues together
    curr1.next = dummy2.next
    # avoid cycle in linked list, since it might include nodes
    # with val less than x 
    curr2.next = None
    return dummy1.next


# build the reversed list from the end
def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reverse_rec(head, prev=None):
    if not head:
        return prev
    node = head.next
    head.next = prev
    return reverse_rec(node, head)


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
    
