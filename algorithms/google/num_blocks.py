# given a doubly linked list and a list of nodes that are in the list, find the number of blocks.
# A block is a group of nodes on the list with references directed at them and adjacent to each other.
def num_blocks(nodes):
    count = 0
    node_set = set(nodes)
    while node_set:
        node = node_set.pop()
        # connect previous nodes if in set
        curr = node
        while curr.prev in node_set:
            curr = curr.prev
            node_set.remove(curr)
        # connect next nodes if in set
        curr = node
        while curr.next in node_set:
            curr = curr.next
            node_set.remove(curr)

        count += 1

    return count
