# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0

        while temp:
            temp = temp.next
            count += 1

        temp = head
        print(count)

        for i in range((count)//2):
            temp =temp.next
        return temp