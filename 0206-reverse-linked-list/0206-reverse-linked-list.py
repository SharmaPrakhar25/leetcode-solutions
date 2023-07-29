# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        
        reversedhead = self.reverseList(head.next)
        tail = reversedhead
        
        if tail is not None:
            while tail.next is not None:
                tail = tail.next
            head.next = None
            tail.next = head
            return reversedhead
        else:
            return head

        
        