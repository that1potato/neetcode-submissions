class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs():
            if len(stack) == 0:
                return 

            x, y = stack.pop()
            visited.add((x, y))
            
            if (x-1, y) not in visited and x-1 >= 0 and grid[x-1][y] == "1":
                stack.append((x-1, y))
            if (x, y-1) not in visited and y-1 >= 0 and grid[x][y-1] == "1":
                stack.append((x, y-1))
            if (x+1, y) not in visited and x+1 < len(grid) and grid[x+1][y] == "1":
                stack.append((x+1, y))
            if (x, y+1) not in visited and y+1 < len(grid[0]) and grid[x][y+1] == "1":
                stack.append((x, y+1))
            
            return dfs()

        counter = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    visited.add((i, j))
                    if grid[i][j] == "1":
                        counter += 1
                        stack = [(i, j)]
                        dfs()

        return counter