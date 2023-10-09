class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        keysOrder = vals.keys()
        total = 0
        
        for charIndex in range(len(s)):
            if charIndex != len(s) - 1 and vals[s[charIndex]] < vals[s[charIndex + 1]]:
                total -= vals[s[charIndex]]
            else:
                total += vals[s[charIndex]]

        
        return total