class Solution:
    def boatsToSavePeople(self, people: list[int], limit: int) -> int:
        people.sort()
        
        res = 0 # number of boats
        l, r = 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1

            while l <= r and remain >= people[l]:
                remain -= people[l]
                l += 1

        return res
    
if __name__ == "__main__":
    s = Solution()
    print("Number of boats: ", s.boatsToSavePeople([1, 1, 1, 1, 5, 5], 7))
    print("Number of boats: ", s.boatsToSavePeople([1, 2], 3))
    print("Number of boats: ", s.boatsToSavePeople([3, 2, 2, 1], 3))