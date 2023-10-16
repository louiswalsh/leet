class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # [[3,2,1],[1,7,6],[2,7,7]]
        cols = []
        print(len(grid))

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cols.append(col)

        answer = 0 
        for row in grid:
            for col in cols:
                if row == col:
                    answer += 1

        return answer

            

