######     Iterative Method
#####     # def reverseList(self, head):
#####         """
#####         :type head: ListNode
#####         :rtype: ListNode
#####         """
######         if head is None:
######             return None
#####
######         nHead = head
######         tail = head.next
######         nHead.next = None
######         while tail is not None:
######             temp = tail.next
######             tail.next= nHead
######             nHead = tail
######             tail = temp
#####
######         return nHead
​