class Solution:
    def findTargetSumWaysBF(self, nums: list[int], target: int) -> int:
        #TODO Need to print all possible ways and not just number of ways
        
        # Using cache mechanism, O(n) = 2 ^ n
        def recursive(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            return recursive(i + 1, total + nums[i]) + recursive(i + 1, total - nums[i])
        
        return recursive(0, 0)
    
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        #TODO Need to write brute force way, O(n) = 2 ^ n

        #TODO Need to print all possible ways and not just number of ways
        
        # Using cache mechanism, O(n) = n * 2 * target
        dp = {} # Key is (index, total); Value is # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))
            
            return dp[(i, total)]
        
        return backtrack(0, 0)
    
if __name__ == "__main__":
    s = Solution()
    print("#Ways to get 3 from [1, 1, 1 ,1 ,1]: ", s.findTargetSumWays([1, 1, 1 ,1 ,1], 3))
    print("#Ways to get 5 from [1, 1, 1 ,1 ,1]: ", s.findTargetSumWays([1, 1, 1 ,1 ,1], 5))
    print("#Ways to get 5 from [1, 1, 1 ,1 ,1]: ", s.findTargetSumWays([1, 1, 1 ,1 ,1], 9))

    print("=========BRUTE FORCE=============")
    
    print("#Ways to get 3 from [1, 1, 1 ,1 ,1]: ", s.findTargetSumWaysBF([1, 1, 1 ,1 ,1], 3))
    print("#Ways to get 5 from [1, 1, 1 ,1 ,1]: ", s.findTargetSumWaysBF([1, 1, 1 ,1 ,1], 5))
    print("#Ways to get 5 from [1, 1, 1 ,1 ,1]: ", s.findTargetSumWaysBF([1, 1, 1 ,1 ,1], 9))
