class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isHappy($n) {
        $arr = array($n => true);
        
        while (true) {
            $strNum = strval($n);            
            $n = 0;
            
            for ($i = 0; $i < strlen($strNum); $i++) {
                $n += $strNum[$i] * $strNum[$i];
            }
                        
            if ($n == 1) return true;
            if ($arr[$n]) return false;
            
            $arr[$n] = true;
    }
}
}