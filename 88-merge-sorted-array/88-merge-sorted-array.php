class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer $m
     * @param Integer[] $nums2
     * @param Integer $n
     * @return NULL
     */
    function merge(&$nums1, $m, $nums2, $n) {
        array_splice($nums1, $m);
        $nums1 = array_merge($nums1, $nums2);
        sort($nums1);
    }
}