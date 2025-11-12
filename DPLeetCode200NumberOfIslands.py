import collections

class Solution:
    def NumberOfIslands(self, nums: list[list[int]]) -> int:
        visited = set()
        islands = 0

        rows = len(nums)
        cols = len(nums[0])

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if(r in range(rows) and
                       c in range(cols) and
                       nums[r][c] == 1 and
                       (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for i in range(rows):
            for j in range(cols):
                if(nums[i][j] == 1 and (i, j) not in visited):
                    bfs(i, j)
                    islands += 1

        return islands
    
if __name__ == "__main__":
    s = Solution()
    nums = [[1, 1, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0]]

    print("Number of islands: ", s.NumberOfIslands(nums))