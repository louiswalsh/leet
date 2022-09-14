class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isIsomorphic($s, $t) {
//         print('THIS IS S
// ');
        $s_array = $this->getArray($s);
//         print($s_array . ' /// ');
//                 print('THIS IS T
// ');
        $t_array = $this->getArray($t);
        // print($t_array . ' /// ');

        if ($s_array == $t_array) {
            return true;
        }
        return false;
    }
    
    function getArray($string) {
        $counter = 0;
        $array = [];
        $chars = str_split($string);
        foreach($chars as $char){
            if (isset($array[$char])) {
                continue;
            } else {
                $array[$char] = $counter;
                $counter = $counter + 1;
            }
        }
        //print_r($array);
        $newStr = '';
        foreach($chars as $char) {
            $newStr .= ' ' . $array[$char];
        }
        return $newStr;
    }
}