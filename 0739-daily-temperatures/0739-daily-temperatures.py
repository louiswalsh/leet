class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        if len(temperatures) == 1:
            return [0]

        stack = []
        results = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            counter = len(stack)
            while counter > 0 and temperatures[i] > stack[counter - 1][0]:
                j = stack[counter - 1][1]
                results[j] = i - j
                stack.pop()
                counter -= 1

                
            stack.append([temperatures[i], i])

        return results