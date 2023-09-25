class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = []
        stack = []

        for letter in s:

            if letter in stack:
                answer.append(stack)
                stack = [letter]
            
            else:
                stack.append(letter)

        if len(stack) > 0:
            answer.append(stack)

        print(answer)
        return len(answer)