public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        int count = 1;

        while( fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast){
                ListNode temp = head;
                while (slow != temp){
                    temp = temp.next;
                    slow = slow.next;
                }

                return slow;
            }
        }

        return null;
    }
}