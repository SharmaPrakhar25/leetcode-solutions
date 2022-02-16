# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        do_swap = False
        temp = None
        temp_arr = []
        node = head
        while node is not None:
            if temp == None:
                temp = node.val
            
            if do_swap:
                temp_arr.append(node.val)
                node.val = temp
                temp = None
            
            do_swap = not(do_swap)
            node = node.next
        
        
        node = head
        do_swap = True
        idx = 0
        while node is not None and idx < len(temp_arr):
            if do_swap:
                node.val = temp_arr[idx]
                idx+= 1
            
            do_swap = not(do_swap)
            node = node.next
        
        return head
            