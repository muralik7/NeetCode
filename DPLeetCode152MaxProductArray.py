class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)
        currMax, currMin = 1, 1

        for i in nums:
            tempMax = i * currMax
            currMax = max(i * currMax, i * currMin, i)
            currMin = min(tempMax, i * currMin, i)

            result = max(result, currMax, currMin)

        return result
    
if __name__ == "__main__":
    s = Solution()
    print("Max Product [-1, -2, -3]: ", s.maxProduct([-1, -2, -3]))
    print("Max Product [5]: ", s.maxProduct([5]))
