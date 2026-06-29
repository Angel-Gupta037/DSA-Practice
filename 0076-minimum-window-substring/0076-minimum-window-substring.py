class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sindex=-1
        minlen=10**5
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1 # Frequency window for t
        l,r=0,0
        cnt=0
        freq={}  # Frequency window for S.
        while r<len(s):
            freq[s[r]]=freq.get(s[r],0)+1
            if s[r] in need and freq[s[r]]==need[s[r]]:
                cnt+=1
                while cnt ==len(need):
                    if (r-l+1)<minlen:  #updatig answer
                        minlen=(r-l+1)
                        sindex=l        
                    freq[s[l]]-=1
                    if s[l] in need and freq[s[l]]<need[s[l]]:
                        cnt-=1
                    l+=1
            r=r+1
        if sindex==-1:
            return ""
        else:
            return s[sindex:sindex + minlen]
            
            
        