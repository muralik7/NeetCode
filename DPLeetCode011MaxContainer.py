class Solution:
    def maximumContainer(self, nums: list[int]) -> int:
        maxWater = 0

        # Brute force
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                volume = (j - i) * min(nums[i], nums[j])
                maxWater = max(maxWater, volume)
        """

        # 2 Pointers
        l, r = 0, len(nums) - 1

        while l < r:
            volume = (r - l) * min(nums[l], nums[r])
            maxWater = max(maxWater, volume)

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return maxWater
    
if __name__ == "__main__":
    s = Solution()
    print("Max Water for [1, 8, 6, 2, 5, 4, 8, 3, 7]: ", s.maximumContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("Max Water for [1, 8, 6, 90, 90, 4, 8, 3, 7]: ", s.maximumContainer([1, 8, 6, 90, 90, 4, 8, 3, 7]))