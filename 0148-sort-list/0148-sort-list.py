class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.middle(head)

        right = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left, right)

    def middle(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        if left:
            curr.next = left
        else:
            curr.next = right

        return dummy.next