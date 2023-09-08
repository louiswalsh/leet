class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        squarePar = ['[', ']']
        circlePar = ['(', ')']
        squiglPar = ['{', '}']

        stack = []

        for i in range(0, len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    if s[i] == ']' and stack[len(stack) - 1] == '[':
                        stack.pop()
                    elif s[i] == '}' and stack[len(stack) - 1] == '{':
                        stack.pop()               
                    elif s[i] == ')' and stack[len(stack) - 1] == '(':
                        stack.pop() 
                    else:
                        stack.append(s[i])

                else:
                    stack.append(s[i])

        return len(stack) == 0
        