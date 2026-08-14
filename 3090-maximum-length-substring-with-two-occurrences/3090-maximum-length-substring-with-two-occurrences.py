class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq={}
        length=0
        l=0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1     #get freq

            while freq[s[r]]>2:
                freq[s[l]]-=1      #reduce count of freq to remian in boundary
                if freq[s[l]]==0:       #if freq becomes 0..delete it
                    del freq[s[l]]
                l+=1        #move left pointer forward 
            length=max(length,r-l+1)
        return length


        