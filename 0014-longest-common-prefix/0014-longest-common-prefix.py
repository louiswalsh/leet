class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        base = strs[0]
        possiblePrefix = ''

        for charIndex in range(len(base)):
            possiblePrefix += base[charIndex]
            print('possible prefix here::: ' , possiblePrefix)

            for otherWord in strs[1:]:
                print('other word between 0 and charIdx', otherWord[0:charIndex + 1])
                if possiblePrefix != otherWord[0:charIndex + 1]:
                    return possiblePrefix[:-1]
                


        return base