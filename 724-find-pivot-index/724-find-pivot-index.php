class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function pivotIndex($nums) {
        //demolish the before
        $before = 0;
        foreach ($nums as $key=>$value) {
            //$before = array_slice($nums, 0, $key);
            $after = array_slice($nums, $key + 1, count($nums) - $key);

            if ($before == array_sum($after)) {
                return $key;
            }
            $before = $before + $value;
        }
        return -1;
        
        
    }
}