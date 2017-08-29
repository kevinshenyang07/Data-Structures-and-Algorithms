# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# reverse k nodes at a time, with k < size of the list
# if the length of a group of nodes is smaller than k, remain as is
# do it with constant space
def reverseKGroup(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode('dummy')
        dummy.next = head
        # usually assign dummy as head
        head = dummy
        while True:
            head = reverseK(head, k)
            if not head:
                break
        return dummy.next

    # head -> n1 -> n2 ... nk -> nk+1
    # =>
    # head -> nk -> nk-1 ... n1 -> nk+1
    # return n1
    def reverseK(head, k):
        # iterated to kth node
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
