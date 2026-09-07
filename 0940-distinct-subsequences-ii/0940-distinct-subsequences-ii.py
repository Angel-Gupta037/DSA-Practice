class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9 + 7
        end=[0]*26
        for ch in reversed(s):
            idx=ord(ch)-97
            total=sum(end)%MOD
            end[idx]=(total+1)%MOD
        return sum(end)%MOD
        