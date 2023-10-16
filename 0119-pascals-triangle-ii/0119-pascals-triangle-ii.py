class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        # [1]
        # [1, 1]
        # [1, 2, 1]
        # [1, 3, 3, 1]
        # [1, 4, 6, 4, 1]

        triangle = [1]

        for _ in range(rowIndex):
            temp = []

            for i in range(len(triangle)):
                if i == 0:
                    temp.append(1)
                else:
                    temp.append(triangle[i] + triangle[i - 1])

            temp.append(1)
            triangle = temp

        return triangle
