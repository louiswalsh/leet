class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        // foreach ($nums as $key=>$value) {
        //     if ($value > $target) {
        //         unset($nums[$key]);
        //     }
        // }
        print_r($nums);
        
        for ($i = 0; $i < count($nums); $i++) {
            for ($j = $i + 1; $j < count($nums); $j++) {
                if ($nums[$i] + $nums[$j] === $target) {
                    return [$i, $j];
                }
            }
        }
        
        //print_r($nums);
        
        
    }
}