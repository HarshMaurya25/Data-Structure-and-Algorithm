class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        return self.solution(head , k)
    
    def solution(self,head , k):
        last = head 
        nxt = None
        prev = None
        i = 0
        
        while last and last.next:
            counter = 0
            temp = last
            while temp:
                counter += 1
                if counter == k: 
                    nxt = temp.next
                    break
                temp = temp.next

            if counter != k:
                break

            first , last = self.reverse(last , prev, k)
            if i == 0:
                head = first
            i += 1
            last.next = nxt
            prev = last

            last = nxt
        
        return head
        
    def reverse(self, head , previous, k):
        curr = head
        count = 0
        prev = previous

        while curr:
            if count >= k:
                break
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1

        if previous != None:
            previous.next = prev
        return [prev, head]