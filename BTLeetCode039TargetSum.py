class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        
        def dfs(i, cur, total):
            # base case
            if total == target:
                result.append(cur[:])
                return
            
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
    
        return result

if __name__ == "__main__":
    s = Solution()
    print("Target sum combinations: ", s.combinationSum([2, 3], 7))