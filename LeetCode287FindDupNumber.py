class Solution:
    def findDupNum(self, nums: list[int]) -> int:
        sum = 0
        maxNumber = len(nums) - 1

        for n in nums:
            sum += n

        return sum - (maxNumber * (maxNumber + 1) // 2)
    
if __name__ == "__main__":
    s = Solution()

    print("Duplicate number: ", s.findDupNum([1, 2, 3, 3, 4]))