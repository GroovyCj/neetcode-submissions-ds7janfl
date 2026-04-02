class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """
        Input:
            A grid matrix which is a list contains lists of 1, 0s
                1 is for land
                0 is for water
                grid[0][0] would represent the first item
                grid[3][4] would represent the last item in the last row
        Output:
            A int that represents the number of islands that exist in the given grid array
            A island is described as an a one that is surrounded by water on its edges horizontally or vertically
            This includes 1's that have a edge that is out of bounds
        Assumptions:
            An island could have a 1 or zero on each one of its sides
            And island can be one contiguous island i.e. its one large mass of islands
                    ["1","1","0","0","1"],
                    ["1","1","0","0","1"],
                    ["0","0","1","0","0"],
                The first block of 1s considered one island
            I think for every point I need to branch out and recursively or iteratively explore every direction that island can move in
            For example I start at 0,0 and explore left, right, up, down,
            Then for each of those directions I explore, left right, up, down, until I hit a zero, and return that
            lets assume out of bounds is a count for water
            I need at least four calls to account for all four directions
        Questions:
            How do I know when to stop searching?  
                I assume I allow a vertex to go into one direction until it hits a zero
                Then wait for the other directions to return to see if they return a truthy response
            Do  I need to start at one point or multiple points?
                Lets say I start at 0,0 how do I branch out from there,
                and do I need to do this for every single point of the grid?
            How do I know exactly when to count the island
            When we are out of bounds is that a count for land or water?
        Approach Ideas:
            I think this is a dfs case, where I need to explore the depth of each island direction first
            I should establish a base case for a recursive command to exit the recursion 
            I need to explore all directions for each point on the grid
            
        """

        visited: set = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    self.dfs(grid=grid, r=r, c=c, visited=visited)
        return count

    def dfs(self, grid: List[List[str]], r: int, c: int,  visited: set) -> None:
        ROW, COL = len(grid), len(grid[0])
     


        if min(r, c) < 0 or r > ROW - 1 or c > COL - 1 or grid[r][c] == "0" or (r, c) in visited:
            return
        

        visited.add((r , c))

        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r , c - 1, visited)
        self.dfs(grid, r , c + 1, visited)