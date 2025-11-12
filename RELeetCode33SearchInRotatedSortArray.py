class Solution:
    def searchInRotSortArray(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted position
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
    
if __name__ == "__main__":
    s = Solution()
    print("Position of target in array: ", s.searchInRotSortArray([1, 2, 3, 4],4))

            
            
                        
            

    