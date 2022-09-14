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
    function reverseList($head) {
        $vals = [];
                
        while ($head->val || $head->val === 0) {
            $vals[] = $head->val;
            $head = $head->next;
        }
        $revVals = array_reverse($vals);
        
        $newHead = new ListNode($revVals[0]);
        $cur = $newHead;
        //print_r($cur);
        print('
');
        for($i = 1; $i < count($revVals); $i++) {
            print_r($revVals[$i] . ' ');
            $newNode = new ListNode($revVals[$i]);
            //print_r($newNode);
            $cur->next = $newNode;
            //print_r($cur->next);
            $cur = $cur->next;
            print('
');
        }
        return $newHead;

    }
}