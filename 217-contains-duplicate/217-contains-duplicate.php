class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function containsDuplicate($nums) {
        $arr = array_count_values($nums);
        
        foreach ($arr as $key=>$value) {
            if ($value > 1) {
                return true;
            }
        }
        return false;
    
    }
}