# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head

        while temp:
            temp = temp.next
            size +=1

        if n > size:
            return head

        pos = size - n

        if pos == 0:
            return head.next

        temp = head
        for i in range(pos - 1 ):
            temp = temp.next
            
        x = temp.next.next
        temp.next = x

        return head
        
