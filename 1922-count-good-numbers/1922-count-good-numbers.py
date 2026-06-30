class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_cnt=(n+1)//2
        odd_cnt=n//2
        res=pow(5,even_cnt,MOD)*pow(4,odd_cnt,MOD)
        return res % MOD




        