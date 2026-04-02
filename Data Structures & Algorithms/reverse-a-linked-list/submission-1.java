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
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode i = head;
        if (i.next == null) {
            return head;
        }
        ListNode j = i.next;
        if (j.next == null) {
            i.next = null;
            j.next = i;
            return j;
        } 
        ListNode k = j.next;

        head.next = null;
        while (k != null) {
            j.next = i;
            i = j;
            j = k;
            k = k.next;
        }
        j.next = i;
        return j;
    }
}
