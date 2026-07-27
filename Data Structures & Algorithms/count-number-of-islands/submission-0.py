class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j])
                if grid[i][j] == "1":
                    islands += 1
                    grid = self.markIsland(i, j, grid)
        
        return islands
    
    def markIsland(self, i, j, grid):
        # Mark 0 with all surrounding 0

        if grid[i][j] == "1":
            grid[i][j] = "0"

            if i+1 < len(grid): self.markIsland(i+1, j, grid)
            if i-1 >= 0: self.markIsland(i-1, j, grid)
            if j+ 1 < len(grid[0]): self.markIsland(i, j+1, grid)
            if j-1 >= 0: self.markIsland(i, j-1, grid)
        
        return grid
                
        