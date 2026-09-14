class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        tail = head
        size = 1

        while tail.next:
            tail = tail.next
            size += 1

        k %= size
        if k == 0:
            return head

        new_tail = head
        for _ in range(size - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        tail.next = head
        new_tail.next = None

        return new_head