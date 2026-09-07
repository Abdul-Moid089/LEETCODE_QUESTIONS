class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        n=len(s)

        dp=[0]*(n+1)
        dp[0]=1

        last=[-1]*26

        for i in range(1,n+1):

            ch=ord(s[i-1])-ord('a')

            dp[i]=(2*dp[i-1])%MOD

            if last[ch]!=-1:
                j=last[ch]

                dp[i]=(dp[i]-dp[j]+MOD)%MOD

            last[ch]=i-1

        return (dp[n]-1) % MOD
