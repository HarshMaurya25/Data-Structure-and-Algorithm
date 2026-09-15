class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        newHead = Node(head.val, head.next)
        head.next = newHead

        temp = newHead.next
        while temp:
            node = Node(temp.val , temp.next)
            temp.next = node
            temp = node.next
        
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        dummy = Node(0)

        prev = dummy
        temp = newHead
        while temp:
            prev.next = temp
            
            if not temp.next:
                break 

            prev = temp
            temp = temp.next.next

        
        return dummy.next
