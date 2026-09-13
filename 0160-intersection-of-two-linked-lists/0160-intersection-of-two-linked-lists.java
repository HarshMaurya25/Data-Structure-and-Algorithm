public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode ans = null;
        ListNode temp = headA;

        while (headA != null){
            headA.val = - headA.val;
            headA = headA.next;
        }

        while (headB != null){
            if (headB.val < 0){
                ans = headB;
                break;
            }
            headB = headB.next;
        }

        headA = temp;
        while (headA != null){
            headA.val = -headA.val;
            headA = headA.next;
        }

        return ans;
    }
}