class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq=[0,0,0]
        l=0
        res=0
        for r in range(len(s)):
            freq[ord(s[r])-ord('a')]+=1
            while freq[0]>0 and freq[1]>0 and freq[2]>0:
                res+=len(s)-r
                freq[ord(s[l])-ord('a')]-=1 
                l+=1
        return res
        