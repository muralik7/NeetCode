class Solution:
    def wordBreak(self, target: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(target) + 1)
        dp[len(target)] = True

        for i in range(len(target) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(target) and target[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
    
if __name__ == "__main__":
    s = Solution()
    wordDict = ["leet", "code"]
    target = input()

    print("leetcode word can be formed from dictionary: ", s.wordBreak(target, wordDict))
                