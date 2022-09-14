class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function runningSum($nums) {
        $sumNums = [];
        $newVal = 0;
        foreach ($nums as $key=>$value) {
            for ($x = 0; $x <= $key; $x++) {
                $newVal = $newVal + $nums[$x];
            }
            $sumNums[] = $newVal;
            $newVal = 0;
        }
        return $sumNums;
    }
}