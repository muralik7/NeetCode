class Solution:
    def longIncSubsequence(self, nums: list[int]) -> int:
        
        # DP - O(n ^ 2)
        # TODO - O(n logn) is possible!!!
        # TODO - Brute force O(2 ^ n) - Find combinations and check if incresing subsequence
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] <= nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
    
if __name__ == "__main__":
    s = Solution()

    print("Longest increasing subswquence: ", s.longIncSubsequence([1, 2, 4, 3]))
    print("Longest increasing subswquence: ", s.longIncSubsequence([1]))
    print("Longest increasing subswquence: ", s.longIncSubsequence([9, 8, 7, 6, 5, 4, 3, 2]))