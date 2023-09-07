class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sList = list(s)
        tList = list(t)

        sList.sort()
        tList.sort()

        return sList == tList