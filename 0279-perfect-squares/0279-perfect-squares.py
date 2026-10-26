class Solution:
    def numSquares(self, n: int) -> int:
        memo ={0:0}
        def solve(x):
            if x in memo:
                return memo[x]

            ans = x

            i=1

            while i*i <=x:
                ans= min(ans,1+solve(x-i*i))
                i+=1

            memo[x]=ans
            return ans

        return solve(n)