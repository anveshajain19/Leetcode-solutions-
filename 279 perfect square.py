class Solution:
    def numSquares(self, n: int) -> int:

        # The dp array.
        dp = [inf] * (n+1)
        
        for i in range(1,n+1):
            
            # calculate the square of i, dp[i_sq] to 1.
            i_sq = pow(i,2)
            if i_sq <= n:
                dp[i_sq] = 1
            
            # dp equation
            for j in range(i):
                dp[i] = min(dp[i],dp[i-j]+dp[j])

        return dp[n]