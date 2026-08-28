class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        coins = sorted(coins)

        def dfs(total):
            if total == amount:
                return 0

            if total in dp:
                return dp[total]
            
            dp[total] = float('inf')
            for c in coins:
                if total + c > amount:
                    break
                dp[total] = min(dp[total], 1 + dfs(total + c))
            return dp[total]
        
        res = dfs(0)
        return res if res < float('inf') else -1