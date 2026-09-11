/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 0;

        ListNode counter = head;

        while (counter != null){
            counter = counter.next;
            count++;
        }

        System.out.println(count);

        int nodePos = count - n;

        if (nodePos == 0){
            return head.next;
        }

        counter = head;
        for (int i = 1 ; i < nodePos ; i++){
            counter = counter.next;
        }

        counter.next = counter.next.next;

        return head;

    }
}