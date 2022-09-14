class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isSubsequence($s, $t) {
        $sArray = str_split($s);
        $tArray = str_split($t);
        $hitCount = 0;
        
        
        
        for($i=0; $i<count($sArray); $i++){
            
            for($j=0;$j<count($tArray); $j++){
                
                if($sArray[$i] == $tArray[$j]){
                    $hitCount++;
                    $i++;
                }
                
                
             
            }
            $j++;
            
        }
        if(count(array_filter($sArray))==0){
            $hitCount = count($sArray);
        }
        return  ($hitCount==count($sArray));
    }
}