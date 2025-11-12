class Solution:
    def wordSearch(self, grid: list[list[str]], target: str) -> bool:
        rows, cols = len(grid), len(grid[0])
        temp = set()

        def dfs(r, c, i):
            if i == len(target):
                return True
            
            if(r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or grid[r][c] != target[i] or (r, c) in temp):
                return False
            
            temp.add((r, c))
            result = (dfs(r + 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c - 1, i + 1))
            temp.remove((r, c))

            return result

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        
        return False
        
if __name__ == "__main__":
    s = Solution()
    target = input()
    grid = [["a", "b", "c"], ["d", "e", "f"]]

    print("String abc exists in grid: ", s.wordSearch(grid, target))

