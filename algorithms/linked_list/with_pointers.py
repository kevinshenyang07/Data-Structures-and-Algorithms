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
