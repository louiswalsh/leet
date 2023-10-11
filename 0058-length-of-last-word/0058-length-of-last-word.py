class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = strip(s)
        sList = s.split(' ')

        return len(sList[-1])