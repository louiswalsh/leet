class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSubArray($nums) {
     
    $currentMax = PHP_INT_MIN;
    $maxEnd = 0;
    
    foreach ($nums as $element) {
        $maxEnd = $maxEnd + $element;
        if ($currentMax < $maxEnd) {
            $currentMax = $maxEnd;
        }
        if ($maxEnd < 0) {
            $maxEnd = 0;
        }
    }
    
    return $currentMax;
}
}