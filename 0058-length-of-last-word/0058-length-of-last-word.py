class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = strip(s)
        sList = s.split(' ')
        print(sList[-1])

        return len(sList[-1])