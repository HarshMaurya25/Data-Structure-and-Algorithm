class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        temp = head.next
        newHead = Node(head.val, None, None)
        prev = newHead

        newNode = {}

        newNode[0] = newHead
        head.val = 0

        i = 1
        while temp:
            node = Node(temp.val , None, None)
            newNode[i]= node
            prev.next = node
            prev = node
            temp.val = i
            temp = temp.next
            i+=1

        temp = head
        newTemp = newHead
        while temp:
            if temp.random:
                randomNode = newNode[temp.random.val]
                newTemp.random = randomNode
            
            temp = temp.next
            newTemp = newTemp.next

        return newHead