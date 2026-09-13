class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = l1;
        int carry = 0;
        ListNode current = null;

        while(l1 != null && l2 != null){
            int val = l1.val + l2.val;
            val += carry;

            l1.val = val % 10;
            carry = val/10;

            current = l1;
            l1 = l1.next;
            l2 = l2.next;
        }

        while (l1 != null){
            int val = carry + l1.val;

            l1.val = val % 10;
            carry = val/10;

            current = l1;
            l1 = l1.next;
        }

        while (l2 != null){
            int val = carry + l2.val;

            l2.val = val % 10;
            carry = val/10;

            current.next = l2;
            current = l2;
            l2 = l2.next;
        }

        while (carry > 0){
            int val = carry % 10 ;
            ListNode temp = new ListNode(val , null);
            carry /= 10;

            current.next = temp;
            current = temp;
        }

        return ans;
    }
}