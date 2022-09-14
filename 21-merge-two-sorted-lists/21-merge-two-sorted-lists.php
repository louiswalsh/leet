/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $list1
     * @param ListNode $list2
     * @return ListNode
     */
    function mergeTwoLists($l1, $l2) {
        if($l1 == null) {
            return $l2;
        } else if($l2 == null) {
            return $l1;
        }

        $head = new ListNode(-1);
        $cur = $head;
        while($l1 != null && $l2 != null) {
            $cur->next = $l1->val <= $l2->val ? $l1 : $l2;
            $cur = $cur->next;
            if($cur->val == $l1->val) {
                $l1 = $l1->next;
            } else {
                $l2 = $l2->next;
            }
        }
        $cur->next = $l1 != null ? $l1 : $l2;
        return $head->next;
    }
}