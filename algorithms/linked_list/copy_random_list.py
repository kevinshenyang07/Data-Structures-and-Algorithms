class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# optimal performance
def copy_random_list(head):
    if not head: return head
    # copy each node and insert right after itself
    curr = head
    while curr:
        node_new = RandomListNode(curr.label)
        node_next = curr.next

        curr.next = node_new
        node_new.next = node_next

        curr = node_next
    # copy random reference
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    # separate out new list
    curr = head
    dummy = RandomListNode(0)
    head_new = dummy
    while curr:
        node_new = curr.next
        node_next = node_new.next

        curr.next = node_next
        head_new.next = node_new

        curr = node_next
        head_new = node_new

    return dummy.next
# O(n) time, O(1) space



# similar to clone graph approach, not good enough in interview
def copy_random_list_mapping(head):
    if not head: return head

    mapping = {}  # original node => copied node

    curr = head
    while curr:
        mapping[curr] = RandomListNode(curr.label)
        curr = curr.next

    curr = head
    while curr:
        mapping[node].next = mapping[node.next]
        mapping[node].random = mapping[node.random]
        curr = curr.next

    return mapping[head]
# O(n) time and space
