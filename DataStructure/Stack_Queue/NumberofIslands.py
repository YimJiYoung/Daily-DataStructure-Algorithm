class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        h, w = len(grid), len(grid[0]) 
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count+=1
        return count
    
    def dfs(self, grid, i, j):
        grid[i][j] = '#'
        for x, y in [(0,1), (1,0), (0,-1), (-1,0)] :
            if (i+x >= 0 and i+x < len(grid) and j+y >= 0 and j+y < len(grid[0]) and grid[i+x][j+y] == '1'):
                self.dfs(grid, i+x, j+y)
