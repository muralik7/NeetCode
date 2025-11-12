class Solution:
    def permutations(self, nums: list[int]) -> list[list[int]]:
        result = []

        # base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutations(nums)

            for perm in perms:
                perm.append(n)
                result.append(perm)
            
            #result.extend(perms)
            nums.append(n)

        return result
    
if __name__ == "__main__":
    s = Solution()
    print("Permutations: ", s.permutations([1, 2, 3]))
