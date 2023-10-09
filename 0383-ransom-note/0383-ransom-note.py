class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        requiredLetters = {}

        for m in magazine:
            if m not in requiredLetters:
                requiredLetters[m] = 1
            else: 
                requiredLetters[m] += 1

        for r in ransomNote:
            if r not in requiredLetters or requiredLetters[r] == 0:
                return False
            
            requiredLetters[r] -= 1

        print(requiredLetters)
        return True