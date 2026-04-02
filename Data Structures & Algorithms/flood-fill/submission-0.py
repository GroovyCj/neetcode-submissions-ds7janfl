class Solution:


    def dfs(self, grid: List[List[int]], r: int, c: int, color: int, visited: set, original_color: int) -> None:
            ROWS, COLS = len(grid), len(grid[0])

            if not (0 <= r <  ROWS and 0 <= c < COLS) or (r , c) in visited or grid[r][c] != original_color:
                return
            
            grid[r][c] = color
            

            visited.add((r,c))
            self.dfs(grid, r - 1, c, color, visited, original_color)
            self.dfs(grid, r + 1, c, color, visited, original_color)
            self.dfs(grid, r , c - 1, color, visited, original_color)
            self.dfs(grid, r , c + 1, color, visited, original_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Input:
            list of list that represent grid points of an image for example
            [[1,1,1],[1,1,0],[1,0,1]]
            to access the first element it would be image[0][0]
            The last would be image[2][2]
            sr = source row
            sc source column
                The starting coordinates of the image
            color: int value to change the coordinate to

        Output:
        a list of list Representing the coordinates that were changed
        Assumptions:
            I must explore each connected pixel that is either horizontal or vertical
                Diagonal is not included
        I must travel through each direction until I meet a pixel that is not color of the original starting point
        I must keep track of what grid coordinates I met
        If this is dfs I must recursive travel through the grid
        I must keep track of what the original color is
        I have to keep track to ensure I do not go out of bounds

        """



        visited: set = set()
        original_color = image[sr][sc]
        if original_color != color:
            visited: set = set()
            self.dfs(grid=image, r=sr, c=sc, color=color, visited=visited, original_color=original_color)        
        return image


        