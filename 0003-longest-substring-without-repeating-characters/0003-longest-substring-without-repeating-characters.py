class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        maxl=0 # what if string is empty
        i,j=0,0
        while j<len(s):
            if s[j] in seen:
                if seen[s[j]]>=i:
                    i= seen[s[j]]+1 #move past the duplicate char
            length =j-i+1
            maxl=max(length,maxl)
            seen[s[j]]=j
            j+=1
        return maxl
        
        