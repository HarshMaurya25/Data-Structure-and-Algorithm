# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = head.next
        temp2 = head
        temp2.next = None

        while temp:
            x = temp.next
            temp.next = temp2
            temp2 = temp
            temp = x
        
        return temp2
