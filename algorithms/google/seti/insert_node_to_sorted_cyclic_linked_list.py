def insert(head, node):
    if not head:
        node.next = node
        return node

    if node.val < head.val:
        tail = head
        while tail.next != head:
            tail = tail.next
        tail.next = node
        node.next = head
        return

    curr = head
    while curr.next != head and node.val > curr.val:
        curr = curr.next

    node_next = curr.next
    curr.next = node
    node.next = node_next
