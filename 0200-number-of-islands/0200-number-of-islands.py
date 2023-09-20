import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque([[r, c]])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                underObs = q.popleft()
                for dRow, dCol in directions:
                    row = underObs[0] + dRow
                    col = underObs[1] + dCol
                    if (row in range(rows)) and (col in range(cols)) and grid[row][col] == "1" and (row, col) not in visited:
                        visited.add((row, col))
                        q.append([row, col])

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r, c))
                    islands += 1
                    bfs(r, c)

        return islands
