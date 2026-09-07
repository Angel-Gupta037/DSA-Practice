class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i=0 #children
        j=0 #cookie 
        cnt=0
        while j<len(s) and i<len(g):
            if s[j]>=g[i]:
                cnt+=1
                i+=1
            j+=1
        return cnt

        