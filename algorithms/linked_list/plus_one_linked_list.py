# Plus One Linked List
# Given a non-negative integer represented as a non-empty singly linked list
# of digits, plus one to the integer.
# assume  the integer do not contain any leading zero, except the number 0 itself
# f(1->2->9) => 130
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # assume head would not be null
        dummy = ListNode(0)
        dummy.next = head
        i = j = dummy  # slow / fast pointers

        while j.next:
            j = j.next
            if j.val != 9:
                i = j
        # i to be the last node with value != 9

        i.val += 1
        while i.next:
            i.next.val = 0
            i = i.next

        return dummy.next if dummy.val == 0 else dummy
