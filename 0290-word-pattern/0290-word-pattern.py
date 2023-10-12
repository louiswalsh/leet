class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        d = {}
        i = 0

        s = s.split(' ')

        if len(pattern) != len(s):
            return False

        while i < len(pattern):
            if pattern[i] not in d.keys() and s[i] in d.values():
                return False
            if pattern[i] in d.keys() and s[i] not in d.values():
                return False
            if pattern[i] in d.keys() and d[pattern[i]] != s[i]:
                return False
            d[pattern[i]] = s[i]
            i += 1

        return True