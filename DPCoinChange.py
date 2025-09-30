class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    solution = Solution()
    result = solution.coinChange(coins, amount)
    print(f"Minimum coins needed: {result}")



