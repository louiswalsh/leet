class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        somethingChanged = False

        rows, cols = len(grid), len(grid[0])

        rotten = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r, c])
                    hasRotten = True
        
        visited = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        timer = 0

        while rotten:
            somethingChanged = True
            for position in range(len(rotten)):
                # [0, 0]
                poppedRotten = rotten.popleft()

                for directionRow, directionCol in directions:
                    obs = [poppedRotten[0] + directionRow, poppedRotten[1] + directionCol]
                    if obs[0] < 0 or obs[0] >= rows or obs[1] < 0 or obs[1] >= cols:
                        continue
                    if grid[obs[0]][obs[1]] == 1 and obs not in visited:
                        visited.append(obs)
                        grid[obs[0]][obs[1]] = 2
                        rotten.append(obs)
            timer += 1
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        if somethingChanged:
            return timer - 1

        return timer


            
