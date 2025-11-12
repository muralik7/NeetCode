class Solution:
    def combinations(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                result.append(subset[:])
                return
            
            # decision to append nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to not append nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)

        return result
    
if __name__ == "__main__":
    s = Solution()
    print("Permutations: ", s.combinations([1, 2, 3, 4]))