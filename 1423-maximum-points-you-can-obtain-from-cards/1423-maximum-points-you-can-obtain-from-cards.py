class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        lsum,rsum,maxsum=0,0,0
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum=lsum
        r=n-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[r]
            r=r-1
            maxsum=max(maxsum, lsum+rsum)
        return maxsum
        

        