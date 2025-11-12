class Solution:
    def twoCityScheduling(self, costs: list[list[int]]) -> int:
        res = 0 # total minimum cost
        diffs = []

        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])

        diffs.sort()

        for i in range(len(diffs)):
            if i < len(diffs) //  2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]

        return res
        
if __name__ == "__main__":
    s = Solution()
    print("minimum cost: ", s.twoCityScheduling([[10, 100], [10, 1000]]))
