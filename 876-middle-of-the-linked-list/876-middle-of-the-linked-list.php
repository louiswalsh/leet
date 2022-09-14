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
     * @param ListNode $head
     * @return ListNode
     */
    function middleNode($head) {
        $ogHead = $head;
        $counter = 1;
        while ($head->next) {
            $head = $head->next;
            $counter = $counter + 1;
        }
    
        $mid = ceil($counter / 2);
        $evenNum = $counter % 2;
        print($counter % 2);
        $counter = 1;
        while ($counter < $mid) {
            $ogHead = $ogHead->next;
            $counter = $counter + 1;
        }
        //print_r($ogHead);
        if ($evenNum == 1) {
            return $ogHead;
        } 
            $ogHead = $ogHead->next;
            return $ogHead;
        }
    
}